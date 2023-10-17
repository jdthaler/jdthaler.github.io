require 'html-proofer'

task :test do
  sh "bundle exec jekyll build"
  options = { :assume_extension => '.html', :ignore_status_codes => [999] ,  :enforce_https => false, :ignore_missing_alt => true}
  HTMLProofer.check_directory('_site/', options).run
end

#:disable_external => true,