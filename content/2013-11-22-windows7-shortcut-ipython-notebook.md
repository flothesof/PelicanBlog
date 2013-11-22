Title: Creating a shortcut to the IPython Notebook server in the Windows 7 file explorer
date: 2013-11-22 14:12
comments: true
slug: IPythonNotebook-shortcut-Windows7-explorer
Tags: Windows 7, IPython Notebook
Category: Python

These days I tend to use the IPython Notebook with pretty much every computational project that I use. At work, I'm using Windows 7. By default, it is quite cumbersome to launch an IPython Notebook in Windows 7. The steps are as follows:

- Navigate to the directory I want to work in
- Right-click, open a shell from the context menu
- Type ipython notebook and press enter

I looked for an even easier right-click and done solution on the internet and couldn't find one. Therefore I wrote my own. As a starting point, I read the tutorial on context menus under Windows 7 at [http://www.howtogeek.com/howto/windows-vista/how-to-clean-up-your-messy-windows-context-menu/](http://www.howtogeek.com/howto/windows-vista/how-to-clean-up-your-messy-windows-context-menu/). From there, I extrapolated the following solution:

- run regedit as an administrator
- open *HKEY_CLASSES_ROOT\Directory\shell*
- create a new key and name it *cmdipynb*
- edit the default string value and change it to *open IPython Notebook server here*
- create a subkey under the *cmdipynb* key and name it *command* 
- edit the default string value and change it to *"C:\Python27\Scripts\ipython.exe" notebook --notebook-dir "%1"*

In case your IPython executable is not located in the *"C:\Python27\Scripts\ipython.exe"* directory, please make changes accordingly.

![IPython Notebook server shortcut in Windows 7]({filename}/images/windows_ipython_notebook_shortcut.png) 
That's it!
