# Postfuscator

> The humans who designed C9 were afraid that the Charvises would disavow their pact.
The humans therefore decided to build an additional defense system, C9, using an ancient programming language. A programming language that Charvises didn’t even know is a programming language!
Can you figure out the correct input?

## Investigating
At first glance we have a simple bash file that will create a new .ps file and takes as only argument a key. After spending a little time reading up on the postscript language specs, the scripts reads pretty easily. What I did was work back from the comparison:

```input encrypt_str test_str``` (line 41)

```encrypt_str``` and ```test_str``` are functions which we will analyze in a sec. ```input``` is a string. The syntax here is basically:

```python
if test_str(encrypt_str(input)) == True:
    print "yes, you got it! flag-"%flag
else:
    print "Sorry, nope."

```

A general characteristic of postscript is the stacked syntax. Basically whatever you want to do you first indicated what vars will be involved then the action. So if you wanted to add a and b you'd say ```a b add```. Keeping this in mind makes reading the code rather intuitive. All we need now is to understand the functions, reverse the whole shabang and it should do the trick.

## Reversing the encrypt_str and test_str

### test_str
Let's start with the second one. Here it is:

```
/test_str {
  /buf_z (800C46E31190C06039198D86E38180DC64311C0D868361C0D47230880C8730F198D06B0F1AC52192188C121C381B8C07039940D86D04898E06638190DC693484C4E092A8B0CA452C9F4961F34958DC6A389A40A691E1A8C643368AC4269010>) def
  /buf 118 string def
  /fake_file buf_z /ASCIIHexDecode filter def
  /fake_file2 fake_file /LZWDecode filter def
  fake_file2 buf readstring
  pop
  pop
  /ok 0 def
  /n 0 def
  {
    /c exch (...) cvs def
    buf n c length getinterval
    c
    eq {/ok ok c length add store} if
    /n n c length add store
  } forall
  ok buf length eq
} def
```

It's pretty straight forward: ```()``` always denotes a string in ps. ```filter``` is the equivalent of ```.encode()```in python. So the first lines take a given string, decode it as hex, decompress this as lzw and read it in buf as a string.

The middle part took me marginally longer to understand but basically ```exch (...) cvs``` used in combination with the ```forall``` will take each character in a string and convert it to it's ordinal value as a string. This value is then compared with buf for the length of itself (which can always be 1,2,3 since the highest ord is 255 and the lowest is 0). If the values are equal, the variable ok is increased by the length.

Finally the function checks if the variable ok is equal to length of buf and returns a bool. Python equivalen below.

```python
def test_str(stri):
    buf_z = '800C46E31190C06039198D86E38180DC64311C0D868361C0D47230880C8730F198D06B0F1AC52192188C121C381B8C07039940D86D04898E06638190DC693484C4E092A8B0CA452C9F4961F34958DC6A389A40A691E1A8C643368AC4269010'
    fake_file = buf_z.decode('hex')
    fake_file2 = lzw.decompress(fake_file)
    buf = ''.join([i for i in fake_file2])
    ok = 0
    n = 0
    for i in stri:
        if str(ord(i)) == buf[n:len(str(ord(i)))]:
            ok += len(str(ord(i)))
         n += len(str(ord(i)))
    if ok == len:
        return True
    else:
        return False

```

### encrypt_str

That is actually a very easy one:

```
/encrypt_str {
  /buf1 65 string def
  /buf2 (4L0ksa1t) def
  /n 0 def
  {
    buf2 n 8 mod get
    xor
    /i exch def
    buf1 n i put
    /n n 1 add store
  } forall
  buf1 0 n getinterval
} def
```

Based on what we've seen so far, the syntax should be relatively easy to understand. It's a very primitive repeating key xor. Python equivalent:

```python
def encrypt_str(stri):
    key = '4L0ksa1t'
    n = 0
    buf = ""
    for i in range(len(stri)):
        buf += chr(ord(stri[i])^ord(key[i%8]))
    return buf
```

## Solving

We're looking for a string that when converted to it's ordinals and joined together will equal the buf in the test_str function. Luckily, the bash file says ```echo $key | tr -Cd a-f0-9 >> postfuscator.ps``` which means all characters that aren't part of the hex alphabet will be stripped. I.e. our input has to be a hex string. We also know from ```/input 65 string def``` that the string can be a maximum of 65 chars long. So all we do is find the candidate with the highest possible ord at each point in order to maximize the space (I agree that was a bit of a leap, the other option was to bruteforce using search trees....). 

I wrote a script that was correct but didn't work for some reason. I spent an insane amount of time (3-4h spread out) trying to understand where I went wrong. Until I reliazed there is a sneaky '%' prepended to the string to be tested. Adding that made it work. Python script below.

```python
buf = '1712009367807218646859018292134521568805686127287089876612468382748236461208592688982686121828975882178245515674851882'
chars = "1234567890abcdefg"
def xor(stri,key):
    return ''.join([chr(ord(stri[i]) ^ ord(key[i%len(key)])) for i in range(len(stri))])

key = '4L0ksa1t'

fir = "%"

def findNext(p,n):
    k = 0
    print "p:%d n:%d\n"%(p,n)
    for i in chars:
        tmp = xor(i,key[p%8])
        if buf[n:n+len(str(ord(tmp)))] == str(ord(tmp)):
            if len(str(ord(tmp))) > k:
                k = len(str(ord(tmp)))
                reti = i
    return reti,k
            
    
            

def solver(p,n,buf,fir):
    
    while n != len(buf):
        tmp,k = findNext(p,n)
        fir += tmp
        n += k
        print n
        print k
        p+=1
    return fir
        

sol = solver(1,2,buf,fir)
```

Et voila, flag is simply the hex part of the string and take the first 20 chars.


