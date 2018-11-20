# Captcha

>Charvises (the native species which lived on Charvis 8HD before the first settlers arrived) were very good at math. In a surprising symbiosis relationship between humans and Charvises, it was agreed that the Charvises would be responsible for C8.
Can you pass their CAPTCHA (Completely Automated Public Turing Test to tell Charvises and Humans Apart)?

## The basics

We are presented with a website containing a simple enough equation composed of addition, substraction, division and multiplication as well as only integers. Easy enough. I laughed to myself as I copied and pasted the string in idle and evaled. And failed. TUrns out this is a nseaky font that maps the 9 digits, plus, minus, slash and parenthesis characters to random other characters. At this point, I saw 2 ways of approaching the problem: OCR and heavy-duty programming.

## OCR
Tesseract is noice but not *that* noice. The idea was to screenshot the page, save as image, run OCR, eval, post request with answer. Easy enough. However, it turned out that even when specifying characters, tesseract simply messes up too often for it to be useful. I tried with higher resolution, different colors etc. etc. but to no avail.

## The long way home: understanding ttf

TTF is ~~a godforsaken garbage format~~ an interesting type of font files developped by apple. [This](https://developer.apple.com/fonts/TrueType-Reference-Manual/) should shed some light on the format. It's fairly straight forward albeit archaic and needlessly boring. The basic idea is that each character is mapped to a glyph which is little more than a collection of coordinates so that it can be correctly rendered. The website gave us a new font file each time which looked like it was auto generated and yielded a new maping each time. I.e. the letter ```c```might be mapped to what looked like 8 and the second time it might be mapped to the letter ```g```. THe glyphs however stayed the same. 

## Solving

From there it was straightforward: take a font file as a tempalte, map the glyphs to the letters displayed on the screen and build a dictionnary. After that send a new request, parse the font file, map each character to it's glyph then use the dictionnary to parse each letter to the actual symbol, eval, submit the request. The python script is self-explanatory.
