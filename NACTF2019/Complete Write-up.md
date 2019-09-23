# NACTF Write-up

##### Table of Contents  
[I General skills](#i-general-skills)  
[II Crypto](#ii-crypto)  
[III Reverse engineering](#iii-reverse-engineering)  
[IV Forensics](#iv-forensics)  
[V Web](#v-web-exploitation)  
[VI Pwn](#vi-pwn)  

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

### 1. Vyom's Soggy Croutons (50, 1012 solves)Loony Tunes
Simple caesar cipher. Use your solver of choice. I like [quipiquip](https://quipqiup.com/)

### 2. Loony Tunes (50, 770 solves)
Another subsitution cipher. There are multiple ways to solve this. The simplest way it to recognize that this is a [pigpen cipher](https://en.wikipedia.org/wiki/Pigpen_cipher) and simply transcribe. But even without getting the hint you can just assign each symbol to an abitrary letter and solve using a subsitution cipher bruter like quipquip.

### 3. Dr. J's Group Test Randomizer: Board Problem #0 (100, 381 solves)
We get a nice long .c file that is some kind of simplified implementation of the [Middle square method](https://en.wikipedia.org/wiki/Middle-square_method). The real implementation actually comes to shine in random3, which I didn't solve in time. Anywho, the only bit we are interested in is the following:

```c
uint64_t nextRand() {
  // Keep the 8 middle digits from 5 to 12 (inclusive) and square.
  seed = getDigits(seed, 5, 12);
  seed *= seed;
  return seed;
}
```

Basically this is a simple series where ```nextRand()``` is dependend on the previous ```nextRand()```. We can reimplement this in python:

```
def digi(d):
    return int(str(d)[4:12])**2
```

And this gets us the correct next number. Full script:

```python

add = 'shell.2019.nactf.com 31425'

s = STTSocket(add)

print s.recv(2048)
print s.recv(2048)

def digi(d):
    return int(str(d)[4:12])**2


def getDigi():
    s.send('r')
    time.sleep(0.5)
    tmp = s.recvline().strip('\n').strip(' ').strip('>')
    return int(tmp)
    

d0 = getDigi()

s.sendline('g')
time.sleep(1)
print s.recv(2048)


for i in range(20):
    d0 = digi(d0)
    s.sendline(d0)
    time.sleep(0.5)
    print s.recv(2048)
```




### 4. Reversible Sneaky Algorithm #0 (125, 405 solves)
Essentially intro to RSA. ```c``` is the ciphertext, ```n``` the modulus and ```d``` the private key. All you need is there:

```hex(pow(c,d,n)))[2:-1].decode('hex')```

### 5. Super Duper AES (250, 139 solves)
This was a fun function. It's a simple implementation of a permutation/substitution. It first convert the string to hex, pads it to a multiple of 4 bytes and breaks it in blocks of 4 bytes, i.e. 8 hex digits. Then there are 2 functions:

```
def substitute(hexBlock):
    substitutedHexBlock = ""
    substitution =  [8, 4, 15, 9, 3, 14, 6, 2,
                    13, 1, 7, 5, 12, 10, 11, 0]
    for hexDigit in hexBlock:
        newDigit = substitution[int(hexDigit, 16)]
        substitutedHexBlock += hex(newDigit)[2:]
    return substitutedHexBlock
    
def permute(hexBlock):
    permutation =   [6, 22, 30, 18, 29, 4, 23, 19,
                    15, 1, 31, 11, 28, 14, 25, 2,
                    27, 12, 21, 26, 10, 16, 0, 24,
                     7, 5, 3, 20, 13, 9, 17, 8]
    block = int(hexBlock, 16)
    permutedBlock = 0
    for i in range(32):
        bit = (block & (1 << i)) >> i
        permutedBlock |= bit << permutation[i]
    return hexpad(hex(permutedBlock)[2:])    
```

It doesn't really matter how many times you perform them, once you reverse them it's easy. So the first one simply substitutes hex digits. If the hex digit is 0, the new digit will be 8 etc. A nice way to reverse it:

```
sub2 = [substituion.index(i) for i in range(16)]
```

your ```substituteRev``` function will be the same as ```substitute``` with the reverse array. And guess what, same thing for ```permuteRev```. All that is left is to reverse the main function (roundRev). The final solution looks like this:

```
def revsub(hexBlock):
    substitutedHexBlock = ""
    sub2 = [15, 9, 7, 4, 1, 11, 6, 10, 0, 3, 13, 14, 12, 8, 5, 2]

    return ''.join([hex(sub2[int(i,16)])[2:] for i in hexBlock])

def revPermute(hexBlock):
    permutation =   [22, 9, 15, 26, 5, 25, 0,
                     24, 31, 29, 20, 11, 17, 28, 13, 8, 21, 30, 3, 7, 27,
                     18, 1, 6, 23, 14, 19, 16, 12, 4, 2, 10]
    block = int(hexBlock, 16)
    permutedBlock = 0
    for i in range(32):
        bit = (block & (1 << i)) >> i
        permutedBlock |= bit << permutation[i]
    return hexpad(hex(permutedBlock)[2:])
    
 def revRound(hexMessage):
    numBlocks = len(hexMessage)//8
    permutedHexMessage = ""
    
    for i in range(numBlocks):
        permutedHexMessage += hexpad(revPermute(hexMessage[8*i:8*i+8]).replace('L',''))

    substitutedHexMessage = ""
    
    for i in range(numBlocks):
        substitutedHexMessage += hexpad(revsub(permutedHexMessage[8*i:8*i+8]).replace('L',''))
     

    return substitutedHexMessage

hexMessage = enc
for i in range(10000):
    hexMessage = revRound(hexMessage)
```

### 6. Reversible Sneaky Algorithm #1 (275, 242 solves)
This one might have a more elegant solution but why go big when you can go home? We know that the flag is ```nactf{abcd}``` where ```a,b,c,d``` are all lowercase letters. So there are only ```26**4 = 456976``` possibilities. We have ```n``` and ```e```. We can just encrypt all possibilities until our encrypted text matches the given cipher.


### 7. Dr. J's Group Test Randomizer: Board Problem #1 (300, 131 solves)
We get a similar .c file as inr random0. But this time, it's not as deterministic since we only get the last 4 digits. I looked at the output for the first 2000 digits. What I realized was that at some point, our output gets to zero and in some cases, remains 0! So simply wait until it happens then send 0 the required number of time. Done.

### 8. Reversible Sneaky Algorithm #2 (350, 98 solves)
Classic [Shor](https://en.wikipedia.org/wiki/Shor%27s_algorithm). We have ```n``` and ```e``` through the ```pem``` file. And we even have ```a```, ```r```. We can actually go through the algorithm and we notice that ```gcd(pow(a,r/2,n)+1,n)``` yields a large number. Bingo, we have a factor.

The added difficulty I found was that in the encryption script we have the following: ```cipher = PKCS1_OAEP.new(key)```. So we must follow the same steps to decrypt. [This](https://www.dlitz.net/software/pycrypto/api/current/Crypto.PublicKey.RSA-module.html) explains how to construct a new RSA key. So the final script is:

```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import long_to_bytes
from fractions import gcd
from RSASolver import *
from are_you_shor import *

key = RSA.importKey(open("oligarchy.pem", "rb"))

n = key.n
e = key.e
p = gcd(pow(a,r/2,n)+1,n)
q = n//p

key2 = RSA.construct((n,e,modinv(e,(p-1)*(q-1))))

cipher = PKCS1_OAEP.new(key2)

cipher.decrypt(long_to_bytes(c))
```

## III Reverse Engineering

## IV Forensics

## V Web exploitation

## VI Pwn


