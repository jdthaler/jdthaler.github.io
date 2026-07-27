# Generates images/preview/, design/preview/ and holiday/preview/ from the
# originals that sit alongside them.
#
# One rule, no exceptions:
#
#   images/foo.jpg           the original -- the only copy of it anywhere
#   images/preview/foo.jpg   generated, sized for how the site displays it
#
# The original is the single source of truth. Replace it, re-run this, and the
# preview follows. Nothing is stored twice, so there is no second copy to forget
# to update.
#
# Which of the two a page uses is an editorial choice this script does not make:
# the front page and about page deliberately show the original, because those
# are the pages people copy an image from, while grids and thumbnails show the
# preview. Links and downloads always point at the original.
#
# Sizes come from the built site rather than being written down here: each <img>
# class is mapped through the $image scale in _sass, CSS background images count
# as spanning the content column, and the largest requirement wins. A preview is
# never larger than its original.
#
# Idempotent: originals are only ever read, so re-running produces identical
# output. To make previews sharper or smaller, change RETINA and re-run.
#
# Run from the repo root, after a build so the display sizes can be read:
#
#   bundle exec jekyll build && python3 _images/make_derivatives.py
#
# Requires Pillow: python3 -m pip install --user Pillow

import glob
import os
import re
import sys

from PIL import Image, ImageOps

# Serve this multiple of the CSS display size, so previews stay sharp on
# high-density screens.
RETINA = 2

# Heights set by the custom classes in _sass/custom.scss, resolved through the
# $image scale in _sass/common/_variables.scss (rem at the 16px root size).
DISPLAY_HEIGHT = {
    "image-h--xl": 320, "image-h--lg": 256, "image-h--sm": 128, "image-h--xs": 64,
    "image-sq--lg": 256, "image-sq--sm": 128,
    "image-96--xl": 320, "image-96--sm": 128, "image-96--xs": 64,
    "image-h": 192,   # the bare class, checked last
}

# The theme's own classes in _sass/common/components/_image.scss set width
# instead. Longer keys match first so image-h--xs is not read as image--xs.
DISPLAY_WIDTH = {
    "image--xl": 320, "image--lg": 256, "image--md": 192,
    "image--sm": 128, "image--xs": 64,
}

# Width of the article content column, from $layout in
# _sass/common/_variables.scss. An image with no size class, or one used as a
# CSS background, can be laid out this wide.
CONTENT_WIDTH = 950

# Directories holding originals. Their preview/ subdirectory is generated.
SOURCE_DIRS = ["images", "design", "holiday"]

JPEG_QUALITY = 82


def preview_path(original):
    directory, name = os.path.split(original)
    return os.path.join(directory, "preview", name)


def originals():
    for directory in SOURCE_DIRS:
        for path in sorted(glob.glob(os.path.join(directory, "*"))):
            if not os.path.isfile(path):
                continue
            if os.path.splitext(path)[1].lower() not in (".jpg", ".jpeg", ".png"):
                continue
            yield path


def displayed_requirements():
    """Map served path -> size requirements read from the built site.

    Each requirement is ("h", px) from a height class, ("w", px) from a width
    class, or ("w", CONTENT_WIDTH) where there is no class to read -- an image
    laid out by its container, or used as a CSS background like the hero banners
    on /engagement and /research. One file can appear several ways: the
    blackboard photo is 128px tall on /press, 64px wide in the credits list, and
    full width on the front page.
    """
    reqs = {}
    for pattern in ("_site/**/*.html", "_site/**/*.css"):
        for path in glob.glob(pattern, recursive=True):
            with open(path, encoding="utf-8", errors="ignore") as fh:
                text = fh.read()
            for tag in re.findall(r"<img[^>]*>", text):
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
            for m in re.finditer(r"url\(\s*[\"']?/+([^\"')]+)", text):
                reqs.setdefault(m.group(1), []).append(("w", CONTENT_WIDTH))
    return reqs


def target_height(original, reqs, aspect):
    """Height the preview should be, from however the site uses either file."""
    wanted = []
    for key in (preview_path(original), original):
        for kind, px in reqs.get(key, []):
            wanted.append(px if kind == "w" else px * aspect)
    if not wanted:
        return None
    return RETINA * max(wanted) / aspect


def main():
    if not os.path.isdir("_site"):
        sys.exit("No _site/ -- run `bundle exec jekyll build` first, so display sizes can be read.")

    reqs = displayed_requirements()
    before = after = 0
    written = 0

    unused = []
    for original in originals():
        preview = preview_path(original)
        os.makedirs(os.path.dirname(preview), exist_ok=True)
        original_size = os.path.getsize(original)

        with Image.open(original) as probe:
            aspect = probe.width / probe.height
        if target_height(original, reqs, aspect) is None:
            # No page shows this image, so a preview would be dead weight --
            # 24 unreferenced alumni portraits were producing 8.5 MB of them.
            # Reference one and re-run; the preview appears.
            unused.append(original)
            if os.path.exists(preview):
                os.remove(preview)
            continue

        with Image.open(original) as raw:
            # Apply any EXIF orientation to the pixels: browsers honour that tag
            # but it does not survive the save, so without this a rotated
            # original comes out upside down in its preview.
            im = ImageOps.exif_transpose(raw)
            target = target_height(original, reqs, im.width / im.height)
            if im.height <= target:
                # No larger than wanted. Still re-encode: an image can be the
                # right size and still enormous from being saved at
                # near-lossless quality.
                width, target = im.width, im.height
                out = im.copy()
            else:
                target = int(round(target))
                width = round(im.width * target / im.height)
                out = im.resize((width, target), Image.LANCZOS)

            if preview.lower().endswith((".jpg", ".jpeg")):
                out.convert("RGB").save(preview, "JPEG", quality=JPEG_QUALITY,
                                        optimize=True, progressive=True)
            else:
                out.save(preview, "PNG", optimize=True)

        # Small files, particularly PNG logos, can come out bigger after a round
        # trip. Keep whichever is smaller; copying verbatim stays deterministic.
        if os.path.getsize(preview) > original_size:
            with open(original, "rb") as src, open(preview, "wb") as dst:
                dst.write(src.read())

        new_size = os.path.getsize(preview)
        before += original_size
        after += new_size
        written += 1
        print("  %-46s %5dx%-5d  %6dKB -> %5dKB" % (
            preview, width, target, original_size // 1024, new_size // 1024))

    if unused:
        print("\n  skipped %d originals no page references (no preview needed):" % len(unused))
        for path in unused:
            print("    %s" % path)

    print("\n  %d previews generated" % written)
    if before:
        print("  originals %.1f MB -> previews %.1f MB  (%.0f%% smaller)" % (
            before / 1e6, after / 1e6, 100 * (1 - after / before)))


if __name__ == "__main__":
    main()
