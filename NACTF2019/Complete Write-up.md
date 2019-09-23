# NACTF Write-up

##### Table of Contents  
[General skills](#i-general-skills)  
[Crypto](#ii-crypto)  

## I General skills

### 1. Intro to flags (10, 1136 solves)
... just input the flag

### 2. Join the Discord (25, 829 solves) 
... flag is on the discord

### 3. What the hex (25, 959 solves)
The text to decode:
>49 20 77 61 73 2e 20 53 6f 72 72 79 20 74 6f 20 68 61 76 65 20 6d 69 73 73 65 64 20 79 6f 75 2e

Simply convert each hex to int and take the corresponding ASCII char. in python:

```''.join(chr(int(i,16)) for i in text.split(' '))```

### 4. Off-base (25, 1025 solves)
The text to decode:
>bmFjdGZ7YV9jaDRuZzNfMGZfYmE1ZX0=

Simply convert from base64

### 5. Cat over wire (50, 908 solves)
Designed to teach the basics to ```netcat```. You can just ```nc``` to the server which will give you the flag.

### 6. Grace's hashbrowns (50, 954 solves)
What we get:
>f5525fc4fc5fdd42a7cf4f65dc27571c

That looks supsiciously like an md5. And even if it doesn't, always google what you get, in many cases you will get an answer. In this case you get the inverse hash from a multitude of websites.


### 7. Cellular Evolution #0: Bellsprout (75, 329 solves)
This was a series of challenges based on a customized cellular automata machine coded in java. Pretty simple conceptially but, as often is with those, yielding a world of different complex behaviours. This first one was straight forward: simply load the input pattern, write the program, parse and step 16 times. The flag is then displayed.


### 8. Get a GREP #0 (100, 764 solves)
I was tempted to to use my newly minted [StringParser](https://github.com/Gdasl/STT/blob/master/StringParser.py) but the file was very small. Easiest is simply to open the zip in a hex editor and search for ```nactf{```. Gets you the flag fast.

### 9. Hwang's Hidden Handiwork (100, 350 solves)
We get 2 files: 1 is the encrypted password, the other a csv, the key. This is a simple subsitution cipher and can be solved as follows:
```
li1 = 'a b ....'.split() #first line of the csv
li2 = 'T v m...'.split()#second line of the csv
d = dict(zip(li2,li1))
''.join(d[i] for i in s)
```
This yields a link where to some image that is very small. You need to change the text of the url to exclude that last part specifying the small size.


### 10. Cellular Evolution #1: Weepinbell (125, 163 solves)
The basic layout of the cells is as follows:

![CellPrinciple](https://github.com/Gdasl/CTFs/raw/master/NACTF2019/Images/cellPrinciple.png)

We look at the instructions and basically just need to reverse them:
- If C == 4, SE should become 3
- If C == 3, SW should become 4
- If C == 2, NE should become 1
- If C == 1, NW should become 2
- If C == 5, leave it

So just write that in compiler language. Don't forget that we always take the POV of the central cell. So the first instruction will actually look at NW, since SE of NW will be C. This program gets the flag:

```
NW == 4: 3
NE == 3: 4
SW == 1 : 2
SE == 2 : 1
5
```


### 11. Get a GREP #1! (125, 589 solves)
There are many ways to Rome here. Essentially a long list of potential flags and we know that the last 7 chars are all vowels. One way to do it is using this code:

```python
f = open('flag(1).txt').read().split()

def isvalid(s):
    al = 'aeiouy'
    for i in s:
        if i not in al:
            return False
    return True


for i in f:
    if isvalid(i[-8:-1]):
        print i
```
It's not elegant but it works!

### 12. Cellular Evolution #2: VikTreebel (150, 90 Solves)
Full disclosure: one of the last challenges I solved. It took a while to wrap my head around it. Essentially, this is like minesweeper as I believe one of the hints mentioned. The ```sum8``` function sums all 8 surrounding cells. So C = N+S+E+W+SE+SW+NE+NW like so:

![Sum8](https://github.com/Gdasl/CTFs/raw/master/NACTF2019/Images/sum8Ex.png)

Given this, we can reverse a single sum8 action as we would solve a game of minesweeper. For instance if C != 0 but any of the surrounding cells are 0, then C == 0 in the original layout. Another example is if we have the following (X denotes a 0):
```
XXX
X3
X3
X3
XXX
```
Then we will have this:
```
XXX
XX1
XX1
XX1
XXX
```
I suggest doing this one on paper, it's a fun exercise and goes relatively fast since most letter are symmetric and some are repeated.

### 13. SHCALC (200, 365 Solves)
Again, probably a bunch of ways to solve this. An easy one is to use backquote subsitution, which will evaluate whatever is in the backquote. So a possible answer would be ``` `cat flag.txt` ```.



## II Crypto


