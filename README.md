How to publish the site
=======================

- copy posts directory to content/posts
- regenerate the site using the pelican command
- push output directory to master branch of flothesof.github.io repository

The pushi to master branch thing should be easy, according to [this link](http://docs.getpelican.com/en/3.3.0/tips.html). 
However, so far, I haven't been able to do it. My current workaround is:

- copy content of output to flothesof.github.io directory
- commit and push the changes to the master branch of the repository

git add *
git commit -m "update site"
git push 


To do
=====

- fix the _nb_header problem
- import old posts
