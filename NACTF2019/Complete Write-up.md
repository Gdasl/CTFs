# NACTF Write-up

## General skills

### 1. Intro to flags (10)
... just input the flag

### 2. Join the Discord (25) 
... flag is on the discord

### 3. What the hex (25)
The text to decode:
>49 20 77 61 73 2e 20 53 6f 72 72 79 20 74 6f 20 68 61 76 65 20 6d 69 73 73 65 64 20 79 6f 75 2e

Simply convert each hex to int and take the corresponding ASCII char. in python:

```''.join(chr(int(i,16)) for i in text.split(' '))```

### 4. Off-base (25)
The text to decode:
>bmFjdGZ7YV9jaDRuZzNfMGZfYmE1ZX0=

Simply convert from base64

### 5. Cat over wire (50)
Designed to teach the basics to ```netcat```. You can just ```nc``` to the server which will give you the flag.

### 6. Grace's hashbrowns (50)
What we get:
>f5525fc4fc5fdd42a7cf4f65dc27571c

That looks supsiciously like an md5. And even if it doesn't, always google what you get, in many cases you will get an answer. In this case you get the inverse hash from a multitude of websites.


### 7. Cellular Evolution #0: Bellsprout (75)
This was a series of challenges based on a customized cellular automata machine coded in java. Pretty simple conceptially but, as often is with those, yielding a world of different complex behaviours. This first one was straight forward: simply load the input pattern, write the program, parse and step 16 times. The flag is then displayed.


### 8. Get a GREP #0 (100)
I was tempted to to use my newly minted [StringParser](https://github.com/Gdasl/STT/blob/master/StringParser.py) but the file was very small. Easiest is simply to open the zip in a hex editor and search for ```nactf{```. Gets you the flag fast.

### 9. Hwang's Hidden Handiwork (100)
We get 2 files: 1 is the encrypted password, the other a csv, the key. This is a simple subsitution cipher and can be solved as follows:
```
li1 = 'a b ....'.split() #first line of the csv
li2 = 'T v m...'.split()#second line of the csv
d = dict(zip(li2,li1))
''.join(d[i] for i in s)
```
This yields a link where to some image that is very small. You need to change the text of the url to exclude that last part specifying the small size.


### 10. Cellular Evolution #1: Weepinbell
Full disclosure: one of the last challenges I solved. It took a while to wrap my head around it. Essentially, this is like minesweeper as I believe one of the hints mentioned. The ```sum8``` function sums all 8 surrounding cells like so:

```

```



