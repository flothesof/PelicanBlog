How to publish the site
=======================

- regenerate the site using pelican
- push ouptut directory to master branch of flothesof.github.io repository

$ pelican content -o output -s pelicanconf.py
$ ghp-import output
$ git push git@github.com:elemoine/elemoine.github.io.git gh-pages:master
