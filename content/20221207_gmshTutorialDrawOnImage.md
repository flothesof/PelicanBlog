Title: GMSH tutorial: how to draw a mesh over an image?
lang: en
date: 2022-12-07 10:05
comments: true
slug: gmsh-draw-over-image
Tags: Software
Category: Python
Image: /images/my-super-image.png # representative-image plugin data, can be deleted
Summary: This post is a tutorial on how to use the meshing program GMSH to draw geometry on top of an image in order to produce a mesh with it.

# What is GMSH?

[GMSH](https://gmsh.info/) is an open-source tool commonly used to produce meshes of geometries in 2D or 3D.
It is both a command line tool and a graphical user interface.

# Drawing a mesh on top of an image

An interesting feature of the graphical user interface is that it can display images as a background to the interactive drawing.
According to the [documentation](https://gmsh.info/doc/texinfo/gmsh.html#General-options), it is possible to include images in JPEG, PNG or PDF format. 

Searching on the internet, I have found a starting point for this tutorial in this post from 2014: http://onelab.info/pipermail/gmsh/2014/009289.html

However, since it is not very explicit, I’ll try to explain a few of the options with associated screenshots.

## Writing a mesh.geo file with a background image (version 1)

If you have an image you want to draw on top, start by creating new `mesh.geo` file with the following lines.

```C++
General.BackgroundImageFileName = "background_image.jpg";
General.BackgroundImage3D = 0; // 2D bg image (if set to 1, will draw in 3D model coordinates)
General.BackgroundImagePositionX = 10; // in pixels (or in model units in 3D case)
General.BackgroundImagePositionY = 10;
General.BackgroundImageWidth = -1; // actual size
General.BackgroundImageHeight = -1; // actual size
```

Once the file has been saved, you can now open it in the GMSH GUI by typing the following at the command line.

```
gmsh mesh.geo
```

Once in the main screen, you should now see your image. 

![v1](/other/gmsh-tutorial/version1.JPG)

## Writing a mesh.geo file with a background image (version 2)

As you may have noticed in the previous image, the 