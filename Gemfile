source "https://rubygems.org"

gem "github-pages", group: :jekyll_plugins
gem "webrick"

gem "rake"
gem "html-proofer"
gem "csv"

# html-proofer 5.2.x extracts zero links when paired with async >= 2.23. Its
# `process_files` starts one async task per file and never resumes them, so the
# checker walks every file, finds nothing, and reports success no matter what is
# wrong with the site. Still present in html-proofer 5.2.1 (latest as of
# 2026-07), so pinning async is the fix. `rake canary` fails if this pin stops
# working, so the suite can never go quietly blind again.
gem "async", "< 2.23"