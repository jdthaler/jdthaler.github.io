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
    # :enforce_https     => false,   # only applies when external checks are on
    :ignore_urls         => [
      "http://v1.jthaler.net/",
      "http://v2.jthaler.net/",
      "http://ctp.mit.edu/",
      "http://wedding.jthaler.net",
      "http://caricesarotti.com/",
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
