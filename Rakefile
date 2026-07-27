require 'html-proofer'
require 'stringio'

# Jekyll's SCSS converter reads through Ruby's default external encoding, which
# is derived from the ambient locale when the process starts. Under a non-UTF-8
# locale -- bare cron, minimal Docker images, some CI runners -- the build dies
# with `Invalid US-ASCII character "\xE2" on line 5`. Reproduce with:
#
#   env -u LANG -u LC_ALL -u LC_CTYPE bundle exec jekyll build
#
# `encoding: utf-8` in _config.yml does not cover this path. The site's content
# genuinely is UTF-8 -- accented author names in papers.yml and talks.yml, curly
# apostrophes in the prose -- so the fix is to declare UTF-8 rather than strip
# characters out of the content. C.UTF-8 is used over en_US.UTF-8 because minimal
# Linux images often ship only the former.
UTF8_LOCALE = 'C.UTF-8'.freeze
unless "#{ENV['LC_ALL']}#{ENV['LANG']}".match?(/utf-?8/i)
  # Applies to anything this Rakefile shells out to, e.g. `jekyll build`.
  ENV['LANG']   = UTF8_LOCALE
  ENV['LC_ALL'] = UTF8_LOCALE
end
# ENV alone cannot fix the already-running process, so set the encoding directly
# for files read in-process (HTMLProofer walking _site).
Encoding.default_external = Encoding::UTF_8

# Shared by the real site check and the canary, so the canary exercises the same
# configuration that `rake test` runs under. Built fresh on each call because
# HTMLProofer mutates the hash it is given.
def proofer_options
  {
    :assume_extension    => '.html',
    :ignore_status_codes => [999],
    # Every rendered image now carries alt, so this check is enforced rather
    # than merely aspirational: a new image without one fails the build.
    # Decorative images and images inside a link that already has a text
    # caption should use alt="" -- that is a real answer, not a missing one,
    # and HTMLProofer accepts it.
    :ignore_missing_alt  => false,
    :disable_external    => true,
    # Hosts exempted from the checks, including enforce_https. Matched as
    # host-anchored regexes rather than literal strings: the previous literal
    # list never matched anything, because the URLs on the site are spelled
    # "http://ctp.mit.edu" while the list said "http://ctp.mit.edu/". That went
    # unnoticed for as long as the checker itself was blind.
    #
    # These stay on http deliberately. Each was probed on 2026-07-27 and has no
    # working HTTPS: either nothing is listening on 443, or the certificate does
    # not validate for that hostname. Linking to https:// would hand visitors a
    # browser security warning, which is worse than plain http.
    :ignore_urls         => [
      %r{^https?://ctp\.mit\.edu},            # connection refused on 443
      %r{^https?://www-ctp\.mit\.edu},        # certificate does not validate
      %r{^https?://www2\.lns\.mit\.edu},      # certificate does not validate
      %r{^https?://www\.physicsmeetsml\.org}, # connection refused on 443
      %r{^https?://video\.albanova\.se},      # connection refused on 443
      # Own legacy sites, on an MIT host serving a self-signed cert.
      %r{^https?://v1\.jthaler\.net},
      %r{^https?://v2\.jthaler\.net},
      %r{^https?://wedding\.jthaler\.net},
      # The site itself is live at https://www.caricesarotti.com, but the bare
      # domain no longer resolves and the two files linked from faq.md are gone
      # (404 under www). Ignored pending a content decision on those two links.
      %r{^https?://caricesarotti\.com},
    ],
  }
end

# HTMLProofer signals failure by calling exit(1) rather than raising, so
# rescuing SystemExit is the only way to ask "did it find anything?" without
# ending the process. Output is captured so that a healthy canary stays quiet.
def proofer_reports_failures?(dir)
  saved_stdout, saved_stderr = $stdout, $stderr
  $stdout, $stderr = StringIO.new, StringIO.new
  begin
    HTMLProofer.check_directory(dir, proofer_options).run
    false
  rescue SystemExit
    true
  ensure
    $stdout, $stderr = saved_stdout, saved_stderr
  end
end

desc "Prove the link checker can still detect a broken page"
task :canary do
  # test/canary/index.html contains one dead link and one missing image.
  #
  # A link checker that silently stops extracting elements reports every build
  # as clean, which is worse than having no check at all. html-proofer 5.2.x
  # does exactly that when paired with async >= 2.23, which is why the Gemfile
  # pins it. This task makes that failure mode loud instead of silent.
  unless proofer_reports_failures?('test/canary')
    abort <<~MSG
      CANARY FAILED: HTMLProofer reported test/canary as clean, but that page
      contains a dead link and a missing image. The link checker is not actually
      checking anything, so `rake test` results cannot be trusted.

      Most likely the `async` pin in the Gemfile has stopped taking effect:
        bundle list | grep async     # must resolve to < 2.23
    MSG
  end
  puts "Canary passed: link checker detects broken links and missing images."
end

# Talk paths as written in _data, paired with the file each one should resolve
# to. Accepts both the bare and leading-slash spellings, matching
# _includes/snippets/get-talk-url.html.
def talk_path_references
  Dir['_data/*.yml'].sort.flat_map do |data_file|
    File.readlines(data_file).each_with_index.filter_map do |line, i|
      next unless (m = line.match(%r{^\s+(?:issue_)?url:\s*(/?talks/\S+)\s*$}))

      { file: data_file, line: i + 1, path: m[1].sub(%r{\A/}, '') }
    end
  end
end

desc "Check that every talk PDF referenced in _data actually exists"
task :talks do
  # These references resolve through site.talks_base_url to GitHub's raw
  # endpoint, which makes them *external* URLs -- so HTMLProofer's internal
  # check cannot see them, by construction, and a missing PDF stays invisible
  # until someone clicks it. (One had been dead on the live site for years; it
  # took an external scan of 1026 links to notice.) Comparing the paths against
  # the filesystem costs nothing and catches the whole class locally.
  refs = talk_path_references
  missing = refs.reject { |r| File.file?(r[:path]) }

  unless missing.empty?
    missing.each { |r| warn "  MISSING: #{r[:path]}  <- #{r[:file]}:#{r[:line]}" }
    abort "\n#{missing.size} of #{refs.size} referenced talk files do not exist. " \
          "Either add the file or drop the url: from the entry."
  end
  puts "Talk files: all #{refs.size} referenced PDFs exist."
end

desc "Build the site and check it for broken links and images"
task :test => [:canary, :talks] do
  sh "bundle exec jekyll build"
  HTMLProofer.check_directory('_site/', proofer_options).run
end

# Deliberately separate from `rake test`, which is meant to gate every push.
# This one reaches out to ~1200 third-party hosts, so it is slow and its result
# depends on the weather: rate limits, bot blocking, and transient 5xx all show
# up as failures. Run it periodically and triage by hand rather than wiring it
# into CI. HTMLProofer retries a failed HEAD as a GET, so servers that reject
# HEAD (docusign.mit.edu, for one) are not reported as dead.
desc "Also check external links (slow, network-dependent; not part of `rake test`)"
task :external => :canary do
  sh "bundle exec jekyll build"
  HTMLProofer.check_directory('_site/', proofer_options.merge(external_options)).run
end

# Tuning for the external run. The first attempt at this reported 518 failures
# out of 1210 links, of which only about a dozen were real; the rest were
# self-inflicted. Three causes, three fixes:
#
#  1. Concurrency. 50 parallel requests across 248 hosts produced 350 timeouts,
#     including 62 against doi.org alone, simply from hammering them. Dropped to
#     10, with longer timeouts, which costs wall-clock and buys signal.
#  2. User agent. HTMLProofer's default agent announces itself and collects 403s
#     from publishers and news sites. A browser agent is what a visitor
#     following the link would send, so it is the honest thing to check with.
#  3. Hosts that block automation regardless. Listed below.
#
# Even tuned, treat a failure here as "look at this by hand", not "this is
# broken" -- re-check with a browser before editing anything.
def external_options
  {
    :disable_external => false,
    :hydra    => { :max_concurrency => 10 },
    :typhoeus => {
      :followlocation => true,
      :connecttimeout => 20,
      :timeout        => 60,
      :headers        => { "User-Agent" => "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) " \
                                           "AppleWebKit/537.36 (KHTML, like Gecko) " \
                                           "Chrome/120.0 Safari/537.36" },
    },
    :ignore_urls => proofer_options[:ignore_urls] + [
      # doi.org resolves correctly; the publishers it redirects to (Wiley,
      # Elsevier and friends) block automated requests, so the DOI is fine even
      # when the check is not. Verified by hand on a sample.
      %r{^https://doi\.org/},
      # Block automation by policy, browser-verified as live.
      %r{^https://www\.nytimes\.com/},
      %r{^https://www\.oecd\.org/},
      # Require an MIT login, so unauthenticated checks can only ever fail.
      %r{^https://stellar\.mit\.edu/},
      %r{^https://canvas\.mit\.edu/},
    ],
  }
end
