# CLAUDE_REVIEW — Technical review of jthaler.net

**Date:** 2026-07-27
**Scope:** Technical (build, delivery, tooling, accessibility, repo health) — **not** content, wording, or design.
**Method:** Read the repo, built the site locally, ran the existing `rake test`, and probed the live site at `jthaler.net` with `curl`. Every claim below has a reproduction command so you can verify it yourself rather than take my word for it.

**Site at a glance:** Jekyll 3.10 via the `github-pages` gem, deployed by GitHub Pages from `main`. A vendored fork of the TeXt theme (`kitian616/jekyll-TeXt-theme`). 24 built HTML pages, driven almost entirely by 18 YAML files in `_data/` — `papers.yml`, `talks.yml`, `mentoring.yml`, `news.yml`, and friends. The data-driven design is genuinely good and is why the site has aged well; most of what follows is about the scaffolding around it, not the architecture.

---

## Status — what has been done since this review was written

Work lives on branches off `main`, in this order: `fix-rake-test`, then `fix-talk-urls` stacked on it.

| item | state | commit |
|---|---|---|
| #2 `rake test` checking nothing | **fixed** — `async` pinned below 2.23, plus a `rake canary` that fails if the checker ever goes blind again | `97e230e` |
| #4 talk URL hardcoding | **partly** — the GitHub `raw` prefix now lives only in `site.talks_base_url`, so the eventual LFS migration is a one-line change. The underlying LFS/Pages problem is untouched. | `17a0f9a` |
| `http://` links (was folded into #10) | **fixed** — 24 switched to https, 9 http-only hosts exempted via host-anchored regexes | `3bbe2e0` |
| dead external links | **mostly fixed** — 5 replaced with working targets; see the outstanding list below | `18a6232` |

`rake test` now passes cleanly: 40 failures to 0, with `enforce_https` still live.

Items **1, 3, 5, 6, 7, 8, 9, 10, 11 remain open.**

---

## Outstanding content items

Content decisions rather than technical work, so they are recorded here rather than guessed at.

### C1. Two dead files linked from `faq.md`

`www.caricesarotti.com` is live, but both files linked from it are gone — 404 even under `www`:

- [faq.md:64](faq.md:64) — `http://caricesarotti.com/n_subjesseness.pdf` ("Token frequency analysis")
- [faq.md:114](faq.md:114) — `http://caricesarotti.com/work.html` ("innovative data analysis strategy")

Left exactly as-is rather than repointed at the homepage, which would change what the links mean. The host is exempted in the `Rakefile` ignore list so the suite stays green; that exemption should come out once these are resolved. The profile link in `_data/mentoring.yml` was separately updated to `https://www.caricesarotti.com/`, which does work.

### C2. `mhsmustangnews.com` article is gone

[_data/news.yml](_data/news.yml) — `https://www.mhsmustangnews.com/2012/10/29/academic-news-mits-jesse-thaler-visits-mhs/` returns 500, and the site root returns 403. Left in place by request. An archive.org snapshot would preserve it if the article matters.

### C3. `hidden.md` hardcodes the year

[hidden.md:12](hidden.md:12) — `{% assign current_year = 2025 %}`. It is now July 2026, so the "Remaining {{year}}" and "Done for {{year}}" email lists have been computing against the wrong year since January. `{{ site.time | date: '%Y' }}` would track by itself. (Moot if the page stops being built per item #1.)

### C4. Alt text needs words

Item #7 covers the mechanical part — 151 of 164 images carry `title` where they need `alt`. The descriptions themselves are an authoring task. The existing `title` values are a reasonable starting point for many of them.

### C5. External links have never been checked

`:disable_external => true` has always been set, and the site has **1,225 unique external URLs**. Everything on this list surfaced incidentally while probing the 32 `http://` links — roughly 3% of the total. A one-off run with external checking enabled would give the real inventory, and is worth doing **before** wiring up CI (#3), so the workflow does not silently adopt whatever is currently broken as its baseline.

Two things learned while probing, worth carrying into that run:

- **`HEAD` requests give false negatives.** `docusign.mit.edu` returns 500 to `HEAD` but 200 to `GET`. Anything the scan flags should be re-checked with `GET` before being called dead.
- **Bot-blocking is not breakage.** `doi.org`, LinkedIn (status 999), and some university personal pages refuse automated requests but work fine in a browser. Expect a batch of false positives to triage into the ignore list.

---

## Tier 1 — Worth acting on soon

### 1. `/hidden` publishes ~72 personal email addresses to the open web

`hidden.md` renders every email in `_data/mentoring.yml` into a public page. It is "hidden" only in the sense that nothing links to it — there is no authentication, no `noindex`, and no `robots.txt`.

```bash
curl -s https://jthaler.net/hidden | grep -coE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
```

Verified: HTTP 200, ~72 unique addresses, no `noindex` meta tag, and `https://jthaler.net/robots.txt` is a 404. Most of those addresses belong to other people — current students, postdocs, and alumni — so the exposure isn't only yours to accept.

**Why it matters:** unlinked ≠ private. Anything reachable by URL gets found by address-bar autocomplete leaks, referrer headers, browser sync, and the crawlers that specifically hunt for unlinked pages. Email harvesting is the concrete risk.

**Suggested fix.** Adding `noindex` helps with search engines but does nothing about anyone who has the URL. The durable fix is to stop publishing the page. The repo already has the right pattern in `_reporting/` — a leading underscore, so Jekyll ignores it, holding local-only tooling that reads `_data/`. Mirror that:

1. Add `hidden.md` to `exclude:` in `_config.yml` so GitHub Pages stops building it.
2. Add a `_config.local.yml` that overrides `exclude:` without that entry, and build locally with
   `bundle exec jekyll serve --config _config.yml,_config.local.yml` when you need the lists.

You keep the exact same page for your own use; it just stops being on the internet. (Note that the addresses will remain in the repo's git history and in any search-engine cache — worth a look at Google Search Console if you want them actively purged.)

Small related bug: line 12 hardcodes `{% assign current_year = 2025 %}`, so the "Remaining {{year}}" / "Done for {{year}}" lists have been computing against the wrong year since January.

---

### 2. `rake test` passes unconditionally — it is checking nothing

This is the one I'd fix first, because everything else depends on it.

```bash
bundle exec rake test
# → "Checking 0 internal links" ... "HTML-Proofer finished successfully."
```

html-proofer reports `Ran on 24 files!` but `Checking 0 internal links`, and finishes in 0.01 seconds. `_site/cv/index.html` alone contains 46 internal and 1109 external links. I confirmed the failure with a canary — a one-line HTML file containing a link to a nonexistent page and an `<img>` pointing at a missing file:

```bash
printf '<html><body><a href="/nope">x</a><img src="/nope.png"></body></html>' > /tmp/t.html
bundle exec htmlproofer /tmp/ --disable-external   # → "finished successfully"
```

It passes. The check extracts zero elements regardless of input, so `rake test` is a green light that means nothing. Nokogiri itself is fine (1.18.10, HTML5 parsing works), so this looks like an html-proofer 5.2.0 incompatibility rather than a config error.

**Why it matters most:** you've said you want to move slowly and build confidence in this new workflow. A working link checker is the mechanism that *earns* that confidence — it's what catches a bad edit before it reaches the live site. Right now there is no such mechanism.

**Suggested fix.** Try a newer html-proofer (5.0.10 and the 6.x line are both worth testing) or swap to `lychee`. Whatever you land on, **add the canary above as a permanent fixture** so the test suite proves it can still fail. A test that cannot fail is worse than no test, because it's actively reassuring.

Two real problems it should be catching once fixed: `:disable_external => true` in the `Rakefile` means the ~1100 external links per page have never been checked, and the ignore list still contains long-dead hosts.

---

### 3. Nothing runs on push — the only workflow is a daily cron

`.github/workflows/republish.yml` is the sole Action, and it just POSTs to the Pages rebuild API every morning at 6am (presumably to refresh the `upcoming`/`today` badges in `_includes/cv/talk_item.html`, which compare against build time). Nothing validates a build or checks links before content goes live.

**Suggested fix.** Once #2 works, add a workflow that runs `bundle exec jekyll build` plus the link check on every push to `main`. Cheap, and it's the guard rail that makes delegating edits to Claude Code safe.

Minor: that workflow grants `permissions: id-token: write`, which it doesn't use — it authenticates with a PAT. Worth dropping.

---

## Tier 2 — Correctness and durability

### 4. Every `jthaler.net/talks/*.pdf` URL serves a 131-byte text file

`.gitattributes` puts `talks/*.pdf` in Git LFS (402 files). **GitHub Pages does not resolve LFS pointers** — it serves the pointer file itself, with a `Content-Type: application/pdf` header that makes it look like a real download.

```bash
curl -sL https://jthaler.net/talks/jthaler_2005_03_NYUSeminar.pdf | head -c 45
# → version https://git-lfs.github.com/spec/v1
```

You already work around this: `_includes/cv/talk_item.html` prepends `https://github.com/jdthaler/jdthaler.github.io/raw/main/` to every talk URL, and `raw.githubusercontent` *does* resolve LFS. So links clicked from your CV page work correctly today — I verified a real PDF comes back.

**The gap is everything that doesn't go through your template:** old bookmarks, citations in other people's slides, links in past emails, and search-engine results all point at `jthaler.net/talks/…` and silently deliver a broken file. Given how long the LFS setup has been in place (January 2023), that's a long tail of dead references.

**Two further fragilities in the current arrangement:**
- Talk downloads bill against your GitHub LFS **bandwidth** quota (1 GB/month on the free tier; you have 4.7 GB of LFS objects, so you're presumably on a paid data pack). Exceeding it doesn't degrade gracefully — every talk link breaks at once.
- Your talk archive is now served by `github.com` rather than by your own domain, so it's outside your control and outside any redirect you might add later.

**Suggested fix.** No urgency, but worth deciding deliberately. The options are (a) accept it and add a redirect rule so the `jthaler.net/talks/…` URLs at least point somewhere useful, (b) move the PDFs off LFS and back into normal git — they'd then serve correctly from your own domain, at the cost of repo size, or (c) host talks on a separate static host or object store. This is a decision to think about, not a change to rush.

---

### 5. The repository is 6.2 GB, and 84% of the history is build output

```bash
du -sh .git          # 6.2G  (4.7G LFS objects + 1.5G packed objects)
du -sh _site         # 4.1G  stale local build output
```

The `_site/` directory was committed until January 2023 (commit `82624f0`, "trying to track better"). Those blobs are still in history:

```
history blob bytes: _site=1.86 GB | other=0.34 GB | total=2.21 GB
```

The largest objects in your repo history are all generated files — a 57 MB `_site/talks/jthaler_2022_03_DarkMatter_LL.pdf`, a 47 MB Boost2018 summary, and so on. A fresh clone pays for all of it.

**Suggested fix.** Two independent, very different actions:
- **Safe and immediate:** delete the local `_site/` directory. It's gitignored, it's stale build output, and it reclaims 4.1 GB. `bundle exec jekyll build` regenerates it in 5 seconds.
- **Deliberate, later, or never:** rewriting history with `git filter-repo` would remove the ~1.9 GB of committed `_site` blobs, but it rewrites every commit hash and requires a force-push. Given a single-maintainer repo the risk is manageable, but this is exactly the kind of change to leave until you're comfortable with the workflow. It is also purely a convenience win — nothing is broken today.

---

### 6. The build fails outright under a non-UTF-8 locale

```bash
env -u LANG -u LC_ALL bundle exec jekyll build
# → Conversion error: ... Invalid US-ASCII character "\xE2" on line 5
```

`assets/css/main.scss` contains non-ASCII bytes, and the old `jekyll-sass-converter` 1.5.2 bundled with Jekyll 3.10 reads it using the ambient locale. It builds fine on GitHub Pages and in your interactive shell, but fails in any environment that doesn't export a UTF-8 locale — cron jobs, Docker, CI runners, and non-interactive tool shells among them. I hit it on my first build attempt in this session.

**Suggested fix.** One line. Either set `ENV['LANG']`/`LC_ALL` at the top of the `Rakefile`, add `env: LANG: en_US.UTF-8` to the CI workflow, or strip the non-ASCII characters from `main.scss`. Worth doing before #3, since CI would otherwise trip over it.

---

## Tier 3 — Quality wins, low risk

### 7. Images use `title=` where they should use `alt=`

59 of the 60 `<img>` tags in your source templates carry a `title` attribute and no `alt`; in the built site that's 151 of 164 images with no alt text.

```bash
grep -rn "<img" --include="*.md" --include="*.html" . | grep -v _site | grep -vc "alt="
```

`title` produces a mouse-hover tooltip. It is not announced reliably by screen readers, never appears on touch devices, and shows nothing if the image fails to load. `alt` is the attribute that does that job. This affects `group.md`, `personal.md`, `press.md`, `index.md`, and the `_includes/cv/` partials.

**Suggested fix.** Largely mechanical — add `alt` alongside the existing `title` (keeping both is fine and often correct). Good first task to hand to Claude Code with a small, reviewable diff, since the change is uniform and easy to eyeball.

### 8. Oversized images

The group page ships **2.3 MB of JPEGs to render five 128-pixel thumbnails**:

| file | size | dimensions | displayed at |
|---|---|---|---|
| `delafuentesimarro.jpg` | 1083 KB | 2632 × 2632 | 128 px |
| `pajarillo.png` | 946 KB | 638 × 661 | 128 px |
| `zhang.jpg` | 170 KB | 1374 × 1394 | 128 px |

(`.image-sq--sm` is `width-sm: 8rem` = 128 px in `_sass/common/_variables.scss:143`.)

Elsewhere, `images/stamp_personal.jpg` is 7.6 MB and `images/alipour-fard.jpg` is 4.2 MB. A single resize pass over `images/` would cut most page weights by an order of magnitude with no visible difference.

### 9. No link previews when the site is shared

```bash
curl -s https://jthaler.net/ | grep -ciE 'og:|twitter:'   # → 0
```

Zero Open Graph and zero Twitter Card tags. Posting a jthaler.net link to Slack, Bluesky, Twitter, or LinkedIn produces a bare URL with no title, description, or image. There's also no `sitemap.xml` (`jekyll-sitemap` is commented out in `_config.yml`, though it *is* supported on GitHub Pages) and no `robots.txt`.

**Suggested fix.** A small `_includes/head/custom.html` addition — that file exists and is empty, clearly intended for exactly this. Roughly 10 lines of Liquid. Note the interaction with item #1: enabling `jekyll-sitemap` before excluding `hidden.md` would advertise that page to every crawler, so do them in that order.

---

## Tier 4 — Structural, for later

### 10. Dependency and theme staleness

- The `github-pages` gem pins **Jekyll 3.10**; Jekyll 4.x has been current for years. GitHub Pages' native build won't move, so upgrading means switching to a GitHub Actions build — real work, real benefit (faster builds, modern Sass, unrestricted plugins), and a good candidate for "once I'm comfortable."
- The theme is a **vendored 2019-era fork** with no upstream link, so it receives no fixes. That's a deliberate and reasonable trade — it's why your customizations survive — but worth naming.
- `_data/variables.yml` loads **jQuery 3.3.1** and **FontAwesome 5.15.1** from third-party CDNs (`unpkg.com`, and `bootcdn.cn` in the unused `bootcdn` profile) with no Subresource Integrity hashes. Self-hosting both would remove a third-party dependency from every page load, drop two DNS lookups, and eliminate a supply-chain vector.
- ~30 `http://` (non-HTTPS) links remain in content, including several that now redirect (`whereis.mit.edu`, `ctp.mit.edu`, `www.linkedin.com`). A fixed link checker (#2) would surface these automatically.

### 11. Config leftovers

Cosmetic, but they'll confuse future-you or any tool reading the repo:
`repository: user_name/repo_name` is still the theme's placeholder; `url:` is blank (GitHub Pages fills it at build time, so canonical URLs are right in production but wrong locally); and `Dockerfile.dev`, `package.json`, and `jekyll-text-theme.gemspec` are unused theme scaffolding. There's no `.ruby-version`, so the build's Ruby version is whatever happens to be on PATH.

---

## Suggested order of operations

Deliberately sequenced so each step makes the next one safer:

1. ~~**Fix `rake test`** (#2), including the deliberately-broken canary fixture.~~ **Done** — `97e230e`.
2. **Fix the locale issue** (#6) — one line, and CI needs it. **Next.**
3. **Run one external link scan** (C5) before CI, so the workflow starts from a known baseline rather than adopting current breakage as normal.
4. **Add build + link-check CI** (#3). Now every change is checked before it's live.
5. **Decide on `/hidden`** (#1). Small change, but it's a judgment call about other people's data, so it's yours to make.
6. **Delete the local `_site/`** (#5, first half). Zero risk, 4.1 GB back.
7. Then the low-risk polish — alt text (#7 and C4), image resizing (#8), meta tags (#9) — which are good first tasks to run through Claude Code, because each produces a small, uniform, easily-reviewed diff.
8. Leave the Jekyll 4 migration, the history rewrite, and the talks-hosting decision until the workflow feels routine. None of them is urgent.

## A note on working with Claude Code here

The `_data/`-driven structure suits this workflow well — most updates are YAML edits with a predictable shape, which are easy to review as diffs. Two things would help:

- **A `CLAUDE.md`** capturing the conventions that aren't obvious from the files: that talk URLs are relative and get the GitHub `raw` prefix applied by the template, that `_reporting/` and `_cv/` are local-only tooling that read `_data/`, and that `_config.yml` needs a server restart. This is a file I can draft for you.
- **Small, single-purpose commits.** The items above are deliberately scoped so each is one reviewable change rather than a sweep.

---

- **A `CLAUDE.md`** — one convention has since changed and is worth capturing: talk paths in `_data/` are written bare (`talks/x.pdf`) and resolved by `_includes/snippets/get-talk-url.html` against `site.talks_base_url`. Note that `url:` and `issue_url:` both carry talk paths, in `talks.yml`, `public.yml`, `service.yml`, and `teaching.yml`.

---

*Findings verified against the live site and a local build on 2026-07-27. Items #1, #2, #4, and #6 were each confirmed by direct reproduction rather than inspection alone; #5's history figures come from `git rev-list --objects --all`. No files were modified in producing the original review, apart from creating this document and adding it to `exclude:` in `_config.yml` so it isn't published to the live site.*

*Updated 2026-07-27 with a status table and the outstanding content items (C1–C5). This document lives only on the `claude-review` branch and is excluded from the Jekyll build, so it is not published — but note the repo is public, so merging this branch to `main` makes it readable on GitHub, including its description of the `/hidden` page. Worth resolving item #1 first.*
