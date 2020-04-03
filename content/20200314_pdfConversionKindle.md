Title: Converting PDF Scans for Optimized Reading on a Kindle 3: a Case-Study
lang: en
date: 2020-03-14 12:07
comments: true
slug: pdf-conversion-kindle3
Tags: DIY
Image: /images/thumbnail_20200314_darwin.png
Category: Python
Summary: I'm still clinging to my Kindle 3 ("Keyboard") ebook reader. I often want to read PDF files that are scanned copies of old books. Since performance easily suffers when using the files as is, I've researched ways to convert the files to a more suitable PDF format.

I received my Kindle 3 (a.k.a. the Kindle Keyboard) almost ten years ago, and it has proven quite durable (even though some parts of the case are now cracked and it's been stained by various liquids...). Since then, I've used it many times to read *old books* in their original format. What I mean by old books are really *classics*, that are now commonly found in the online libraries of the world (my favourite is of course [Gallica](https://gallica.bnf.fr/), but there are many others, e.g. [Europeana](https://www.europeana.eu/portal/en), [Deutsche Nationalbibliothek](https://www.dnb.de/DE/Professionell/ProjekteKooperationen/DDB/ddb_node.html), [archive.org for books and texts](https://archive.org/details/texts)).

One of the recurring problems I have is to convert the PDFs from these online libraries to a format usable on my Kindle. Searching for solutions has taken me to the scripts and tips I'm using below. I'll try to make a case study using the origin of the species found [here](https://gallica.bnf.fr/ark:/12148/bpt6k6564680d/f9.image). I'll call this file `darwin.pdf` and will try to convert it to various formats, comparing file sizes. The file we start with is a 145 MB PDF with color scans.

# Ghostscript

The main tool I will use is [Ghostscript](https://ghostscript.com/), a free "interpreter for the PostScript language and for PDF". In my test below, I'll use the latest available version on MacOS: Ghostscript 9.51.

I found a lot of conflicting information about the use of Ghostscript online. I now realize this is probably due to the fact that PDF is a really complicated file format. And that there is a lot going on between the actual raster images embedded before they get rendered to the screen, which explains why there isn't an option to "just compress the images more".

## First script: using /ebook and converting to grayscale

A first script to test the conversion is to use the built-in PDF settings designed for ebook use.

We can use it like this:

```shell
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -o darwin1.pdf darwin.pdf
```
## Second script: adding grayscale conversion

However, my Kindle can only use grayscale, so let's add a flag for grayscale.

```shell
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -dColorConversionStrategy=/Gray -dProcessColorModel=/DeviceGray -o darwin2.pdf darwin.pdf
```

## Third script: manually setting the DPI

A last option is to manually set the DPI you want so that the image data gets converted.

```shell
gs -sDEVICE=pdfwrite -dColorConversionStrategy=/Gray -dProcessColorModel=/DeviceGray -dDownsampleGrayImages=true -dGrayImageResolution=72 -dGrayImageDownsampleThreshold=1.0 -o darwin3.pdf darwin.pdf 
```

## Comparison

Here's a table with the obtained file sizes and usability.

| File        | File size | Usability on Kindle 3 (subjective) |
|-------------|-----------|------------------------------------|
| darwin.pdf  | 145.6 MB  | Good                               |
| darwin1.pdf | 91.5 MB   | Very good (faster page turning)    |
| darwin2.pdf | 85.4 MB   | Very good (faster page turning)    |
| darwin3.pdf |  80.8 MB  | Very good (faster page turning)    |

So I have to say that these conversion scripts are quite good. But still, the grayscale image is not very high contrast so it would be great to have a thresholded image.

# Other tricks

In the course of the conversion process, I've also found that if you want to crop the images you can use the native MacOS Preview app as described here: http://hints.macworld.com/article.php?story=200711012305556.

# Useful links

- A discussion of Ghostscript options for resizing: https://gist.github.com/firstdoit/6390547
- A Python app that shrinks images in an EPUB: https://github.com/murrple-1/epub-shrink (linked by https://ebooks.stackexchange.com/questions/6772/how-can-i-reduce-the-resolution-of-images-in-an-epub-or-mobi-file)

# Conclusion

This is a first step for conversion. However, I'm still missing a binarization step where the books get converted to 4 bit grayscale. Maybe this would be possible using the above script epub-shrink process but that would be for another time. 