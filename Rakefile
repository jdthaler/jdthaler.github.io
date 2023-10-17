require 'html-proofer'

task :test do
  sh "bundle exec jekyll build"
  options = { :assume_extension => '.html', :ignore_status_codes => [999] ,  :ignore_missing_alt => true, :disable_external => true, :ignore_urls => ["http://v1.jthaler.net/", "http://v2.jthaler.net/", "http://ctp.mit.edu/", "http://wedding.jthaler.net", "http://caricesarotti.com/"]}
  HTMLProofer.check_directory('_site/', options).run
end

#:enforce_https => false, 