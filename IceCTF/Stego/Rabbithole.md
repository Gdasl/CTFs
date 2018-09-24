# Rabbit Hole

> Here's a picture of my favorite vegetable. I hope it doesn't make you cry.

## The setup
We get a simple jpg of an onion. We know it's stego so I started poking there. It took me a very very large amount of time to find it, even thought the fact that it's a jpg seriously limited the possbilities. 

## The solving

##Part 1: Extracting from jpg
It ended up being an image processed with steghide. Now all I needed was the password. After some trial and error and remembering the harshells debacle, I ended up trying 'onion' which was correct. I then got a textfile containing a seemingly random string of printable chars.

##Part 2: Onion
The name is a give away: it's a website on the onion network which can be accessed through tor. Not necessarily eager to venture there, I used a web proxy to access the page, which turned out to be a gigantic chunk of chinese characters, as well as some gifs.

##Part 3: Reading Chinese
Funny enough, I read chinese and this was basically junk. At this point it was also around 2am on a work night and I was getting slowly but surely a little tired. My first instict was to separate the stuff, i.e. dump the whole chinese chunk in a binary file, extract the gifs as png and start by performing basic stego on the latter. It didn't yield anything so I turned my attention to the cinese text again. No, from previous challenges I had done some extensive readup on multi-byte encodings and my first thougth was that it could be just that. Alas, none of the usual suspects seemed to fit. So I started wandering. Talking to other people, one directed my attention towards bases, such as base64. Given the size however, it had to be something else. 3 am came and went and that's basically when I discovered that there exists such a thing as [base65536](https://github.com/qntm/base65536). It turned out to be right.

##Part 4: Mooom, are we there yet?
Almost. Decoding the blob using base65536 and ddumping it in a binary file finally gave us something recognizable: a PKZIP file. Upon opening it, I was greeted by some dubious ebook which, quite frankly, I simply wans't equipped to deal with at the taime of the night. I had an instant regret the next morning when I simply ran ```strings``` on the file and immediately got the flag.

To summarize: this was one of the best challenges I've come accross. Incredibly creative and a lot of new things learned, and also very lucrative, part of what brought me in the top20. 11/10 would do again.
