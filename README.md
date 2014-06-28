How this repository works
=========================

This repository is used to generate the content for the blog at [http://flothesof.github.io](http://flothesof.github.io). It works with the help of *git submodules* for three critical parts of the blog:

- the plugins directory
- the theme directory
- the IPython Notebooks used as the main content of this blog (they can be found at [https://github.com/flothesof/posts](https://github.com/flothesof/posts))

Some help concerning *git submodules* can be found at the following link: [http://chrisjean.com/2009/04/20/git-submodules-adding-using-removing-and-updating/](http://chrisjean.com/2009/04/20/git-submodules-adding-using-removing-and-updating/).

How to publish the content of this site
=======================================

- write content in an IPython post
- update submodule with posts
- create a markdown file for the post
- publish and check that the output is correct
- make deploy from the command line to push to flothesof.github.io
