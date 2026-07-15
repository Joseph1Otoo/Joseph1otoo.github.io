source "https://rubygems.org"

# The site is built and deployed by GitHub Actions (.github/workflows/pages.yml),
# not by the Pages built-in builder, so we are not pinned to Jekyll 3.9.
gem "jekyll", "~> 4.3"
gem "minima", "~> 2.5"

group :jekyll_plugins do
  gem "jekyll-seo-tag", "~> 2.8"
  gem "jekyll-sitemap", "~> 1.4"
end

# Windows and JRuby do not include zoneinfo files.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Left stdlib in Ruby 3.4; Jekyll still needs them.
gem "csv"
gem "base64"
gem "bigdecimal"
