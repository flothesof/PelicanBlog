Title: Installing sms-tools under Mac OS X and Anaconda 
date: 2015-09-28 22:42
comments: true
slug: sms-tools-MacOSX-Anaconda
Tags: Anaconda, MOOC, Mac OS X 
Category: Python
Summary: This post is dedicated to installing the sms-tools software suite using a virtual environment made with Anaconda under Mac OS X. 

I've just started following an online class entitled [Audio Signal Processing for Music Applications on Coursera](https://www.coursera.org/course/audio).

In this course, the student is asked to use a software package called sms-tools, which is openly available through Github.

Unfortunately, the installation instructions for this software package are, at the moment of writing, not tailored to the OS X operating system. This is partly due to the way that the course was designed, as the recommended operating system is Linux.

In fact, this does not matter, as we will see in this tutorial that one can setup the software on a Mac using Anaconda. 

# What is Anaconda?

Anaconda is a scientific Python distribution that aims at replacing systems such as pip, virtualenv and Python installations already present on your system. 

One of the cool things about it is that it provides you with all major scientific packages without you needing to care how to install them (NumPy, SciPy...).

# Step by step tutorial

## Cloning the sms-tools repository

The first step is to clone (a fancy technical word for copy or download) the sms-tools software repository on your local hard drive.

I choose to work in a directory called workspace where I created a specific folder for this Coursera class. 

The cloning is done using the following command:

```
git clone https://github.com/MTG/sms-tools.git
```

## Creating a new conda environment with Python 2.7

Once you've downloaded the software package, it's time to create a virtual environment for sms-tools.

What is a virtual environment? It's a sort of sandbox within which you'll work with specific versions of Python and its packages, so as not to interfere with your system Python.

Assuming you already have Anaconda setup, it's really easy to do:

```
conda create -n sms python=2.7 ipython numpy matplotlib scipy cython
```

The previous command tells conda to create a new environment using Python 2.7 and installing the packages that follow. The reason we install these packages is that they're needed by the sms-tools.

## Compiling the Cython code parts

Now that we have a new environment with all the packages we need, let's activate it. We need to do this every time we want to work with the course tools:

```
source activate sms
```

This command should slightly alter the prompt which now usually looks like this for me:

```
(sms)kappamaki@Florians-MBP:~/workspace%
```

The (sms) part means that I have activated the right environment.

Let's now switch to the directory where we put the sms-tools from earlier. In my case I type:

```
(sms)kappamaki@Florians-MBP:~/workspace% cd coursera-aspma/sms-tools/software/models/utilFunctions_C/
```

Once I'm in that directory, I need to type the following:

```
(sms)kappamaki@Florians-MBP:~/workspace/coursera-aspma/sms-tools/software/models/utilFunctions_C% python compileModule.py build_ext --inplace
```

Once I hit enter, I get several warnings and a message that the Cython code was compiled.

This is it, we're done!

## If you run into trouble

When I first tried to compile the Cython code, I wound up with a weird error that said:

````
/Users/kappamaki/workspace/coursera-aspma/sms-tools/software/models/utilFunctions_C/utilFunctions_C.so
ld: library not found for -lgcc_s.10.5
clang: error: linker command failed with exit code 1 (use -v to see invocation)
error: command 'gcc' failed with exit status 1
````

After googling this error, in particular the line starting with "ld:", I needed to do the following before compiling again:

```
cd /usr/local/lib
sudo ln -s ../../lib/libSystem.B.dylib libgcc_s.10.5.dylib
```

After that, it should work fine. 

# Wrap-up

In this post, we went through the steps needed to install the sms-tools package from Github, in the frame of a Coursera class.

I assumed that you have already Anaconda installed on Mac and used it to create a virtual environment called `sms` with Python 2.7 (although Python 3 should now be standard).

I initially had compiling errors, but I hope the solution I wrote down will help other people running into the same error.

Happy musical coding!
