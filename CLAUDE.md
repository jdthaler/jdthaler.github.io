# Working on jthaler.net

Jekyll site, hand-built over many years, on a vendored fork of the TeXt theme.
JT's preference, stated at the outset and worth honouring: **change things slowly
and deliberately.** Small single-purpose commits that read cleanly as diffs.

## Branches and deploy

- Work on `main`. Push there freely.
- **The site deploys from `live`, and `live` is not to be touched directly.**
  `main` reaches it by pull request, which JT opens and merges. He says "live
  went live!" when it has happened.
- GitHub Pages builds `live` with its legacy builder, which pins **Jekyll 3.10**
  via the `github-pages` gem. Jekyll 4 would mean building in Actions instead —
  a real change to how the site ships, deliberately deferred.

## Before pushing

1. `bundle exec rake test` — canary, then talk-PDF existence, then html-proofer
   over the built site. It must be green.
2. **Kill any `jekyll serve` first.** A running server rewrites `_site` with
   `localhost:4000` URLs and produces a stream of phantom failures. The Rakefile
   detects this and aborts, but it costs a build to find out.
3. Update whatever record the work belongs to (see *Records*, below) **in the
   same batch of commits** — not as a catch-up afterwards.

`rake external` checks third-party links. It reaches ~250 hosts, fails on their
rate limits rather than on anything here, and is deliberately kept out of
`rake test` and out of CI. Run it by hand, occasionally.

CI (`.github/workflows/test.yml`) runs `rake test` on pushes to `main` and on PRs
into `live`. It checks out with `lfs: false` on purpose — see *Talks*.

## Verifying template changes

**`rake test` cannot tell you whether a template change was correct.** It checks
links, image existence and alt attributes. It cannot see a Liquid whitespace bug,
an image at the wrong size, or an image upside down. Every such regression in
this repo's history was caught by JT looking at a page.

So for any change to a template, include, or `_data` loop:

```bash
bundle exec jekyll build -q --destination /tmp/before   # at HEAD
# make the change
bundle exec jekyll build -q --destination /tmp/after
diff -r /tmp/before /tmp/after
```

For a pure refactor the correct result is **byte-identical output**. For a change
with intended effects, every differing line should be one you can name in advance.

One built-in exception: `news.md` renders `{{ "now" | date }}` as a "Last updated"
line, so `news/index.html` differs between two builds taken on different days.
That one line is expected noise; anything else is not.

### Liquid traps that have actually bitten here

- A **trailing newline in an include** becomes a blank line between list items,
  so kramdown emits a *loose* list with every entry wrapped in `<p>`.
  `_includes/cv/public_entry.html` and `_includes/design_cell.html` deliberately
  end without one.
- **`-%}` strips the leading whitespace of the next line**, which may be a list
  indent or a grid cell's indent. Note `{%- assign entry = include.entry %}` in
  `public_entry.html` — the missing closing dash is load-bearing.
- A **bullet immediately after `{% endfor -%}`** lands mid-line, so the next
  bullet is parsed as a nested sublist. Flush-left bullets avoid it.
- **`size` is a Liquid built-in** returning a hash's key count. A data field
  named `size` renders as a number. `_data/design.yml` uses `height` for this
  reason.
- `include` takes a **variable name**, not `{{ }}` interpolation or a filter chain.
- `_includes/snippets/page-url.html` **prints** the absolute URL rather than
  assigning it, so `__return` after including it holds only the path. Use
  `prepend-baseurl.html` plus `site.url` when you need an absolute URL.
- `_config.yml` is not reloaded by `jekyll serve`; restart it.

## Content lives in `_data/`

Nineteen YAML files drive nearly everything — `papers.yml`, `talks.yml`,
`news.yml`, `bio.yml`, `mentoring.yml`, `design.yml`, `holiday.yml` and so on.
Most updates are YAML edits, which is the point: they review cleanly as diffs.

**When adding text that a `_data` file could hold, put it there rather than in
markup** — including alt text. JT asked for this explicitly after alt strings
were hardcoded into templates for images whose captions already lived in YAML.

## Images

Originals live in place: `images/`, `design/`, `holiday/`, `news/`. Each has a
generated `preview/` subfolder beside it holding the downscaled version actually
served.

**After adding or replacing an image, run `python3 _images/make_derivatives.py`.**
It reads the built HTML to find the display size of each image, generates only
what pages reference, and is idempotent. Notes:

- It uses `ImageOps.exif_transpose`, because PIL reads raw pixels and drops the
  orientation tag — without it, EXIF-rotated photos ship upside down.
- It scans CSS `url()` as well as `<img>`, because hero images are CSS
  backgrounds and were missed the first time.
- **The front page and `/about` deliberately use full-size originals, not
  previews** — people copy images straight from those pages.

`ignore_missing_alt` is off, so every rendered image needs alt text and CI
enforces it. Empty `alt=""` is a legitimate answer for an image whose caption or
surrounding prose already says the same thing.

## Talks

`talks/*.pdf` is **Git LFS**, and GitHub Pages does not resolve LFS — it serves
the 131-byte pointer file. So talk links do not point at this site. They are
rewritten through `site.talks_base_url` (in `_config.yml`) by
`_includes/snippets/get-talk-url.html`, which prepends GitHub's raw endpoint to
any path whose first directory is `talks`. If talks ever leave LFS, set that one
value to `/` and every link on the site follows.

CI checks out with `lfs: false` deliberately: the PDFs come to ~3.7 GB, LFS
bandwidth is metered, and `rake talks` only asks whether each path exists — an
unsmudged pointer is a real file, so the check works identically without them.

## `_config.yml`

**Setting `exclude:` REPLACES Jekyll's built-in exclude list rather than adding
to it.** Verified by building with `/vendor` removed and a file planted in
`vendor/bundle/`, which was copied straight into `_site`. So `Gemfile`,
`Gemfile.lock`, `/node_modules` and `/vendor` must stay listed even though Jekyll
excludes them by default. `/vendor` is the one that would bite, and it would bite
in CI, where `bundler-cache` installs every gem there.

**Anything added at the repo root that is not site content — a notes file, a
record, a script — needs an `exclude:` entry, or Jekyll publishes it.** A file
with no front matter is not skipped; it is copied verbatim into `_site` and
served. `TODO` was public at `https://jthaler.net/TODO` from the day it was
created until 27 July 2026, unlinked but readable by anyone who asked for it.
Nothing warns you: the build succeeds and `rake test` passes.

## Local-only tooling, and privacy

`_cv/` (LaTeX CV) and `_reporting/` (annual reporting) read the same `_data/`
YAML and are **not part of the site build**. `_reporting/parse_yaml_emails.py`
writes `email_lists.txt`, which is gitignored and must stay that way.

**This repository is public.** `_data/mentoring.yml` contains contact details for
78 people, tracked in the open by JT's explicit decision. Do not widen that: no
new addresses in tracked files, and nothing that aggregates them.

## Known oddities

- `aaron/`, `ania/` and `dedushka/` are 310-byte `meta refresh` stubs preserving
  pre-Jekyll URLs, pointing at `/aaron.html` and friends. `design/` had a fourth
  whose target had been deleted, so the old URL bounced to a 404; it was removed
  on 28 July 2026 and `/design/` now 404s directly. The portfolio renders from
  `_data/design.yml` inside `personal.md`. **html-proofer does not follow
  meta-refresh**, so `rake test` will never check the three that remain.
- `sywt/index.html` is a genuine standalone 747 KB page, linked from nowhere and
  reachable only by direct URL.
- `_data/variables.yml` loads jQuery and FontAwesome from CDNs with no SRI.
  jQuery is not a `<script src>` — the theme injects it at runtime — so it cannot
  take an integrity attribute without self-hosting.

## Records

- **`TODO`** — JT's own list of content and feature ideas. His file, his words.
- **`docs/review-2026-07.md`** — frozen record of the July 2026 technical review:
  what was wrong, what was done, and why each decision went the way it did.
  Historical; do not edit. Item #10 is the one thing it leaves open.
