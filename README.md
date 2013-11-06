How to publish the site
=======================

## Rough method

- copy posts directory to content/posts
- regenerate the site using the pelican command
- push output directory to master branch of flothesof.github.io repository

## Manual method

- pelican
- ghp-import output
- git push -f https://github.com/flothesof/flothesof.github.io.git gh-pages:master

## Automatic method

- make github

To do
=====

- fix the _nb_header problem
- import old posts
