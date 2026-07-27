# Regenerates the web-sized images the site serves, from full-resolution masters.
#
# Why: several served images were far larger than the slot they display in.
# design/jthaler_BOOST2019_Poster.png was 8.7 MB at 3300x5100 pixels to fill a
# 128-pixel-tall thumbnail, and /personal carried 17.9 MB of images in total.
#
# Nothing is lost and resizing is reversible, because every derivative is
# generated from a master this script only ever reads. There are two patterns,
# and which one applies is an editorial question, not a technical one: does a
# visitor have any business downloading the full-resolution file?
#
#   Master published, derivative alongside in preview/
#     For images whose high-resolution version is meant to be downloadable: the
#     press photos, and anything a visitor clicks to see properly.
#       images/foo.jpg          full resolution, the download or link target
#       images/preview/foo.jpg  what the page actually displays
#
#   Master hidden under _images/, derivative served at the original path
#     For images nobody needs at full size: colleagues' portraits, decorative
#     thumbnails that link somewhere else, institutional logos. Jekyll does not
#     publish underscore directories, which is why _data/, _cv/ and _reporting/
#     are absent from the live site.
#       _images/masters/images/foo.jpg   full resolution, never served
#       images/foo.jpg                   what the page displays
#
# Idempotent: masters are never written to, so re-running produces identical
# output. To resize back up, change RETINA (or the CSS) and re-run.
#
# Run from the repo root, after a build so display sizes can be read:
#
#   bundle exec jekyll build && python3 _images/make_derivatives.py
#
# Requires Pillow: python3 -m pip install --user Pillow

import glob
import os
import re
import sys

from PIL import Image, ImageOps

# Serve this multiple of the CSS display size, so images stay sharp on
# high-density screens.
RETINA = 2

# Display heights the image classes set, from $image in
# _sass/common/_variables.scss (rem values at the 16px root size). Kept here
# rather than as per-file numbers so targets follow the markup: restyle an image
# and its derivative size follows on the next run.
DISPLAY_HEIGHT = {
    "image-h--xl": 320, "image-h--lg": 256, "image-h--sm": 128, "image-h--xs": 64,
    "image-sq--lg": 256, "image-sq--sm": 128,
    "image-96--xl": 320, "image-96--sm": 128, "image-96--xs": 64,
    "image-h": 192,   # the bare class, checked last
}

# The theme's own classes, in _sass/common/components/_image.scss, set width
# instead. Longer keys are checked first so image-h--xs is not mistaken for
# image--xs. Missing these was what inflated the press thumbnails: an
# unrecognised class looks class-less, and a class-less image is assumed to fill
# the column.
DISPLAY_WIDTH = {
    "image--xl": 320, "image--lg": 256, "image--md": 192,
    "image--sm": 128, "image--xs": 64,
}
# Width of the article content column, from $layout in
# _sass/common/_variables.scss. An image with no size class can be laid out
# this wide, so that is the requirement it implies.
CONTENT_WIDTH = 950

# Masters whose full-resolution version stays published, with the displayed copy
# generated into a preview/ subdirectory. Listed explicitly because "should this
# be downloadable?" is a judgement about each image, not something to infer.
PUBLISHED_MASTERS = [
    "images/jthaler_mit_spotlight.jpg",   # press download + /index hero
    "images/jthaler_photo_2017.jpg",      # press download + /about hero
    "images/stamp_personal.jpg",          # /personal hero, linked to full size
    "design/jthaler_IAIFI_Banner.jpg",    # already links to itself
]

# (master glob, function from master path to the derivative it produces)
GROUPS = [
    ("_images/masters/design/*.png", lambda m: os.path.join("design", os.path.basename(m))),
    ("_images/masters/images/*",     lambda m: os.path.join("images", os.path.basename(m))),
    ("holiday/*.jpg",                lambda m: os.path.join("holiday/preview", os.path.basename(m))),
]
for _m in PUBLISHED_MASTERS:
    GROUPS.append((_m, lambda m: os.path.join(os.path.dirname(m), "preview", os.path.basename(m))))

JPEG_QUALITY = 82


def displayed_requirements():
    """Map served image path -> list of size requirements from the built HTML.

    Each requirement is ("h", px) from a size class, or ("w", px) for an image
    with no size class, which is laid out by its container and so can be as wide
    as the content column. The same file can appear both ways: the blackboard
    photo is 128px tall on /press but fills the column on the front page, and
    sizing it for /press alone shrank the hero to 671px inside a 950px column.
    They are resolved to widths later, once the image's aspect ratio is known,
    and the largest wins.
    """
    reqs = {}
    for root, _dirs, files in os.walk("_site"):
        for name in files:
            if not name.endswith(".html"):
                continue
            with open(os.path.join(root, name), encoding="utf-8") as fh:
                html = fh.read()
            for tag in re.findall(r"<img[^>]*>", html):
                src = re.search(r'src="/+([^"]+)"', tag)
                if not src:
                    continue
                classes = re.search(r'class="([^"]*)"', tag)
                classes = classes.group(1) if classes else ""
                height = next((v for k, v in DISPLAY_HEIGHT.items() if k in classes), None)
                width = next((v for k, v in DISPLAY_WIDTH.items() if k in classes), None)
                if height is not None:
                    req = ("h", height)
                elif width is not None:
                    req = ("w", width)
                else:
                    req = ("w", CONTENT_WIDTH)
                reqs.setdefault(src.group(1), []).append(req)

            # Images referenced from CSS rather than markup, such as the hero
            # banner on /engagement. There is no class to read and the element
            # spans at least the content column, so they get that requirement.
            # Missing these shrank that banner to 128px wide, because the file's
            # only <img> use is a 64px credit thumbnail on /press.
            for m in re.finditer(r"url\(\s*[\"\']?/+([^\"\')]+)", html):
                reqs.setdefault(m.group(1), []).append(("w", CONTENT_WIDTH))
    return reqs


def target_height(derivative, master, reqs, aspect):
    """How tall the derivative should be, or None if nothing references it.

    Checks the derivative's own requirements first, then the master's, which is
    what pages reference until the markup is switched over.
    """
    for key in (derivative, master):
        if key in reqs:
            widths = [px if kind == "w" else px * aspect for kind, px in reqs[key]]
            return RETINA * max(widths) / aspect
    return None


def main():
    if not os.path.isdir("_site"):
        sys.exit("No _site/ -- run `bundle exec jekyll build` first, so display sizes can be read.")

    reqs = displayed_requirements()
    before = after = 0
    resized = skipped = 0

    for pattern, derivative_of in GROUPS:
        for master in sorted(glob.glob(pattern)):
            if os.path.isdir(master):
                continue
            derivative = derivative_of(master)
            if os.path.abspath(derivative) == os.path.abspath(master):
                continue
            os.makedirs(os.path.dirname(derivative), exist_ok=True)

            master_size = os.path.getsize(master)
            with Image.open(master) as raw:
                # Apply any EXIF orientation to the pixels. Browsers honour that
                # tag, but PIL reads raw pixels and the tag does not survive the
                # save, so without this a rotated master -- stamp_personal.jpg is
                # tagged 180 degrees -- comes out upside down in its derivative.
                im = ImageOps.exif_transpose(raw)
                target = target_height(derivative, master, reqs, im.width / im.height)
                if target is None or im.height <= target:
                    # Already no taller than wanted. Still worth re-encoding:
                    # images can be the right size and yet enormous because they
                    # were saved at near-lossless quality -- stamp_qcd.jpg was
                    # 536 KB at 900x600. Re-encoding always starts from the
                    # master, so this stays idempotent.
                    width, target = im.width, im.height
                    out = im.copy()
                else:
                    target = int(round(target))
                    width = round(im.width * target / im.height)
                    out = im.resize((width, target), Image.LANCZOS)

                old = os.path.getsize(derivative) if os.path.exists(derivative) else master_size
                if derivative.lower().endswith((".jpg", ".jpeg")):
                    out.convert("RGB").save(derivative, "JPEG", quality=JPEG_QUALITY,
                                            optimize=True, progressive=True)
                else:
                    out.save(derivative, "PNG", optimize=True)
                new = os.path.getsize(derivative)

            # Some already-small files, particularly PNG logos, come out bigger
            # after a round trip. Keep whichever is smaller; copying the master
            # verbatim is still deterministic.
            if new > master_size:
                with open(master, "rb") as src, open(derivative, "wb") as dst:
                    dst.write(src.read())
                new = os.path.getsize(derivative)

            before += old or os.path.getsize(master)
            after += new
            resized += 1
            print("  %-46s %5dx%-5d  %6dKB -> %5dKB" % (
                derivative, width, target, (old or os.path.getsize(master)) // 1024, new // 1024))

    print("\n  wrote %d, skipped %d" % (resized, skipped))
    if before:
        print("  %.1f MB -> %.1f MB  (%.0f%% smaller)" % (
            before / 1e6, after / 1e6, 100 * (1 - after / before)))


if __name__ == "__main__":
    main()
