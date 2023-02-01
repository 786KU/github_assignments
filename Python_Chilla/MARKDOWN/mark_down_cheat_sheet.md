# 1 - Headings

How to give headings in markdown file?

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
You can give headings upto 6 # tag

# 2 - Block of words/citation
This is a normal text.
> This is a block of special text.
>
> This is second line. 
# 3 - Line Breaks
This is a 40 days long course Data Science with Python AKA

 Python ka Chilla with Baba Ammar. \ 

This is a second line.\
Line break can be given with a single/double enter or \ sign.

# 4 - Combine two things

Block of words and headings

> ## Heading 2

# 5- Face of text

**Bold** 

*Italic* 

***Bold and italic***

or you can use following signs

__Bold__

_Italic_

___Bold and Italic___

# 6 - Bullet points or list
- Day1
- Day2
- Day3
- Day4
- Day5
- Day6
    - Day-6a
        - Anything
    - Day-6b
- Day7
- Day8

For numbering

1. Day1
2. Day2
2. Day3
2. Day4
2. Day5
2. Day6

    2. Day-6a
    2. Day-6b
2. Day7

you can copy and paste and it knows that it needs to put numbering.

You can make a list of numbering using * or #

__using */+__
* day 1
+ day 2

# 7 - Line/Page breaks
This is page 1.

---
___
***

This is page 2.
# 8-  Link and Hyperlinks
The following is the link.

<https://www.youtube.com/@Codanics> 

The following is Hyperlink, i.e., text is showing and link is attached into it behind.

[This is the link for Codanics channel](https://www.youtube.com/@Codanics)

You can make a key to the link by following:

[Codanics]:https://www.youtube.com/@Codanics

The channel link to Baba Ammar is [here][codanics].

# 9 - Images and figures with link

To join this course, please scan the qr code using the follwoing image.

The following will open the image via the link as before.

[QR](QR.png)

The follwing will show the image.

![QR](QR.png)


> How to comment a markdown? And what is its shortcut key? find it?

To give a link to an online image:

![Codanics](https://www.google.com/search?q=codanics&sxsrf=AJOqlzX0GeG0sQzOUkuq7gu0Rdgi_iDHTQ:1675022550133&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjhnd2gye38AhWZ8LsIHUovD4MQ_AUoAXoECAIQAw&biw=1366&bih=568&dpr=1#imgrc=jSNIAJI341a1QM)


# 10 - Adding code or code block

To print a string use, `print("Codanincs")`

`print("Hello Mr. Dawood")`

Now to add a code block (use this, its more convenient): 

> This code will show colors according to pyhton language syntax
```python
x=5+6
y=3-1
z=x-y
print(z)
```
> This code will show colors according to R language syntax

```R
x=5+6
y=3-1
z=x-y
print(z)
```
> This code will show colors according to html language syntax
```html
x=5+6
y=3-1
z=x-y
print(z)
```

# 11 - Adding tables

| species | petal_length | sepal_length |
|:----|:----:|----:|
|virginca|19.3|10.2|
|setosa|12.3|9.2|
|virginca|19.3|15.2|
|versicolor|17.8|12.7|


# 12- Contents 

[1- Headings](#1---headings)

[2- block-of-words/citations](#2---block-of-words)

[3- line-breaks](#3---line-breaks)

[4- combine-two-things](#4---combine-two-things)

[5- face-of-text](#5--face-of-text)

[6- bullet-points-or-list](#6---bullet-points-or-list)\
[7- linepage-breaks](#7---linepage-breaks)\
[8- link-and-hyperlinks](#8---link-and-hyperlinks)\
[9- images-and-figures-with-link](#9---images-and-figures-with-link)\
[10- adding-code-or-code-block](#10---adding-code-or-code-block)\
[11- adding-tables](#11---adding-tables)

When you will click on any content in the preview file, you will be moved to that secion automatically.

# 13- Install extensions now

After installing extensions, you will see that you can do all these stuff using keyboard shortcuts, e.g., for bold, press ctrl+b, etc.,

**sample text**

_italic_

_**Bold and Italics**_

[Link](https://www.youtube.com/@Codanics)


Column A | Column B | Column C
---------|----------|---------
 A1 | B1 | C1
 A2 | B2 | C2
 A3 | B3 | C3


Column A | Column B | Column C
---------|----------|---------
 A1 | B1 | C1
 A2 | B2 | C2
 A3 | B3 | C3

convert this file to all formats and see the results. 

Then, you will observe that, you can not copy from the block of codes, there will be no option available in the corner. However, this would be possible with a html file. But still, it will not work. However, finally, it will work when you will paste your code on the GitHub!  

# 14- How to give chnage the color of a line:

<span style="color:green">
This is a colored line.
</span>

you can give any name or even a color code from hexa color

# 15- Adding equations in Markdown

> in-line math

$this_{is}^{inline}$

> Math block
$$ 
\int_0^\infty\frac{x^3}{e^x-1}\,dx=\frac{\pi^4}{15}
$$ 

Further you can search how to write these equations from [Math Jacks](https://docs.mathjax.org/en/latest/) or [MyST Markdown overview](https://jupyterbook.org/en/stable/content/myst.html)


Here is the link to the source from where we learned all this.

[Visual Studio Link to Mark down language](https://code.visualstudio.com/docs/languages/markdown)