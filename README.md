![Build status](https://github.com/flothesof/PelicanBlog/actions/workflows/python-build-deploy-pelican-blog.yml/badge.svg)

How this repository works
=========================

This repository is used to generate the content for the blog at [http://flothesof.github.io](http://flothesof.github.io). It works with the help of *git submodules* for three critical parts of the blog:

- the plugins directory (from [https://github.com/getpelican/pelican-plugins](https://github.com/getpelican/pelican-plugins))
- the IPython Notebooks used as the main content of this blog (they can be found at [https://github.com/flothesof/posts](https://github.com/flothesof/posts))

How to publish the content of this site
=======================================

## Create content

- write content in an IPython post, commit changes to submodule posts and push them
- create a markdown file for the post, add it to tree
- add changes from posts submodule to update tree to latest version
- commit changes and push

## Build

Manual build:
- make publish: generates output for site
- make deploy: push to github (Windows)
- make deploy_mac: push to github (Mac)

Or automatic build with Github actions on every push (check .github/workflows/python-build-deploy-pelican-blog.yml for details).


Cheetlist for Working with submodules
=====================================

I've had quite a lot of trouble working with submodules. Below is a short summary of what I learnt.

## Adding a submodule to this blog

Example for the octopress theme:

```
$git submodule add https://github.com/duilio/pelican-octopress-theme.git pelican-octopress-theme 
```

This also clones the repo and adds the files to the tree, so you can directly commit changes to your branch.

I originally followed these explanations concerning the submodules: [http://chrisjean.com/2009/04/20/git-submodules-adding-using-removing-and-updating/](http://chrisjean.com/2009/04/20/git-submodules-adding-using-removing-and-updating/).

## Deleting submodules

This is done manually. A good tutorial is here: [https://davidwalsh.name/git-remove-submodule](https://davidwalsh.name/git-remove-submodule).
