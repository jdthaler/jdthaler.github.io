# Regenerates the web-sized images the site serves, from full-resolution masters.
#
# Why this exists: several served images were enormously larger than the size
# they display at -- /design/jthaler_BOOST2019_Poster.png was 8.7 MB at
# 3300x5100 pixels to fill a 128-pixel-tall slot, and /personal carried 17.9 MB
# of images in total.
#
# Nothing is lost, and resizing is reversible, because every derivative is
# generated from a master that this script only ever reads:
#
#   served                        master                              also linked as
#   design/*.png                  _images/masters/design/*.png        design/*.pdf (vector)
#   holiday/preview/*.jpg         holiday/*.jpg                       the click-through target
#
# Masters live under _images/, which Jekyll never publishes -- the same reason
# _data/, _cv/ and _reporting/ are absent from the site. To go back up, change
# RETINA below (or the CSS) and re-run; the masters are untouched, so this is
# idempotent and can be run as often as you like.
#
# Run from the repo root, after a build so that _site/ exists:
#
#   bundle exec jekyll build && python3 _images/make_derivatives.py
#
# Requires Pillow: python3 -m pip install --user Pillow

import glob
import os
import re
import sys

from PIL import Image

# Target this multiple of the CSS display size, so the images stay sharp on
# high-density screens. 2 is the usual choice.
RETINA = 2

# Display heights the .image-h--* classes set, from $image in
# _sass/common/_variables.scss (rem values at the 16px root size). Keeping this
# here rather than hardcoding per-file sizes means the targets follow the markup:
# restyle an image and its derivative size follows on the next run.
DISPLAY_HEIGHT = {
    "image-h--xl": 320,   # 20rem
    "image-h--lg": 256,   # 16rem
    "image-h--sm": 128,   # 8rem
    "image-h--xs": 64,    # 4rem
    "image-h": 192,       # 12rem, the bare class
}
FALLBACK_HEIGHT = 192

# served glob -> how to find that file's master
GROUPS = [
    ("design/*.png", lambda p: os.path.join("_images/masters/design", os.path.basename(p))),
    ("holiday/preview/*.jpg", lambda p: os.path.join("holiday", os.path.basename(p))),
]

JPEG_QUALITY = 82


def displayed_heights():
    """Map each served image path to the tallest height any page displays it at.

    Read from the built HTML rather than declared by hand, so the numbers cannot
    drift away from the markup. An image shown at several sizes gets the largest.
    """
    heights = {}
    for root, _dirs, files in os.walk("_site"):
        for name in files:
            if not name.endswith(".html"):
                continue
            with open(os.path.join(root, name), encoding="utf-8") as fh:
                html = fh.read()
            for tag in re.findall(r"<img[^>]*>", html):
                src = re.search(r'src="/([^"]+)"', tag)
                if not src:
                    continue
                classes = re.search(r'class="([^"]*)"', tag)
                classes = classes.group(1) if classes else ""
                # --xl before the bare class, so "image-h image-h--xl" matches --xl.
                height = next(
                    (v for k, v in DISPLAY_HEIGHT.items() if k in classes),
                    FALLBACK_HEIGHT,
                )
                path = src.group(1)
                heights[path] = max(heights.get(path, 0), height)
    return heights


def main():
    if not os.path.isdir("_site"):
        sys.exit("No _site/ -- run `bundle exec jekyll build` first, so display sizes can be read.")

    heights = displayed_heights()
    before = after = 0
    resized = skipped = 0

    for pattern, master_of in GROUPS:
        for served in sorted(glob.glob(pattern)):
            master = master_of(served)
            if not os.path.isfile(master):
                print("  no master, left alone:  %s" % served)
                skipped += 1
                continue

            target = RETINA * heights.get(served, FALLBACK_HEIGHT)
            with Image.open(master) as im:
                if im.height <= target:
                    # Master is already no bigger than we want; copying it would
                    # only re-encode and lose a little quality for nothing.
                    print("  master already small: %s" % served)
                    skipped += 1
                    continue
                width = round(im.width * target / im.height)
                out = im.resize((width, target), Image.LANCZOS)
                old = os.path.getsize(served)
                if served.lower().endswith((".jpg", ".jpeg")):
                    out.convert("RGB").save(served, "JPEG", quality=JPEG_QUALITY,
                                            optimize=True, progressive=True)
                else:
                    out.save(served, "PNG", optimize=True)
                new = os.path.getsize(served)

            before += old
            after += new
            resized += 1
            print("  %-44s %5dx%-5d  %6dKB -> %5dKB" % (
                served, width, target, old // 1024, new // 1024))

    print("\n  resized %d, skipped %d" % (resized, skipped))
    if before:
        print("  %.1f MB -> %.1f MB  (%.0f%% smaller)" % (
            before / 1e6, after / 1e6, 100 * (1 - after / before)))


if __name__ == "__main__":
    main()
