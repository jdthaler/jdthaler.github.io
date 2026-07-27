require 'html-proofer'
require 'stringio'

# Shared by the real site check and the canary, so the canary exercises the same
# configuration that `rake test` runs under. Built fresh on each call because
# HTMLProofer mutates the hash it is given.
def proofer_options
  {
    :assume_extension    => '.html',
    :ignore_status_codes => [999],
    :ignore_missing_alt  => true,
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

desc "Build the site and check it for broken links and images"
task :test => :canary do
  sh "bundle exec jekyll build"
  HTMLProofer.check_directory('_site/', proofer_options).run
end
