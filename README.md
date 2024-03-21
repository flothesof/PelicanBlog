![github actions build status](https://github.com/flothesof/PelicanBlog/actions/workflows/python-build-deploy-pelican-blog.yml.yml/badge.svg)

How this repository works
=========================

This repository is used to generate the content for the blog at [http://flothesof.github.io](http://flothesof.github.io). It works with the help of *git submodules* for three critical parts of the blog:

- the plugins directory (from [https://github.com/getpelican/pelican-plugins](https://github.com/getpelican/pelican-plugins))
- the ~~IPython~~ Jupyter Notebooks used as the main content of this blog (they can be found at [https://github.com/flothesof/posts](https://github.com/flothesof/posts))

How to publish the content of this site
=======================================

## Create content

- write content in a Jupyter notebook, commit changes to submodule `posts` and push them
- create a markdown file for the post in `content` (typically by copypasting `content\template`), including the previously authored Jupyter notebook, add it to tree
- add changes from `posts` submodule to update tree to latest version
- commit changes and push

## Build

Manual build:
- `pelican`   

Serve locally after build:
- `pelican -l`

Other options:
- `make deploy` (deploys built site) 
## Continuous integration 

An automatic build with Github actions is done on every push (check `.github/workflows/python-build-deploy-pelican-blog.yml` for details).
If the build is successful, it is also deployed to the blog website.


Cheatlist for Working with submodules
=====================================

I've had quite a lot of trouble working with the `pelican-plugins` submodule. Below is a short summary of what I learnt.

## Adding a submodule to this blog

Example for the octopress theme:

```
$git submodule add https://github.com/duilio/pelican-octopress-theme.git pelican-octopress-theme 
```

This also clones the repo and adds the files to the tree, so you can directly commit changes to your branch.

I originally followed these explanations concerning the submodules: [http://chrisjean.com/2009/04/20/git-submodules-adding-using-removing-and-updating/](http://chrisjean.com/2009/04/20/git-submodules-adding-using-removing-and-updating/).

## Deleting submodules

This is done manually. A good tutorial is here: [https://davidwalsh.name/git-remove-submodule](https://davidwalsh.name/git-remove-submodule).
