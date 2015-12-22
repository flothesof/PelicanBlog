Title: Autodeploying this blog with Travis 
date: 2015-12-22 14:46
comments: true
slug: autodeploy-with-Travis
Tags: Pelican, Travis-CI
Category: Python
Summary: In this post, I explain how I got Travis-CI to work with this blog. 

# What is Travis-CI?

Travis-CI is a company that offers continuous integration services (CI: hence the name). Continuous integration is a set of routines that get applied to your source code once you commit new changes. 
It turns out that when you openly host your material on GitHub, you can use Travis for free. In particular, I thought that it would be nice to automate my blog's deployment using Travis.

# How does it work?

I use [Pelican](http://getpelican.com) for this blog. This means that I first write my posts, then generate static HTML and then push it to GitHub, which hosts it and displays it to browsers connecting to my github.io domain.
Instead of pushing the changes manually to github.io, Travis takes care of this for me now. Every time Travis sees a new commit, he generates the HTML and pushes it to the server.

# Was it difficult to set up?

I must admit I had a hard time to get it working. A few things I learnt along the journey follow:

- OAuth token encryption: For Travis to be able to push to your github repo, he must have the rights to do this. I chose the way of the OAuth token. You tell GitHub to give you a token, which allows anyone having it to push to your repos.
- I use git submodules in my blog. Adding --recursive to a clone command automatically clones them for me. That's really neat.
- I have a setup that needed a little tweaks before it worked: I have a repo for my blog source ([https://github.com/flothesof/PelicanBlog](https://github.com/flothesof/PelicanBlog)) and an output repository ([https://github.com/flothesof/flothesof.github.io](https://github.com/flothesof/flothesof.github.io)). I therefore had to adapt the build part to this. 

# Helpful links

I couldn't have mastered the difficulties I faced without the helpful links of people that did something similar. I particuly recommend two links:

- [http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html](http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html)
- [http://zonca.github.io/2013/09/automatically-build-pelican-and-publish-to-github-pages.html](http://zonca.github.io/2013/09/automatically-build-pelican-and-publish-to-github-pages.html)


