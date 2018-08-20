# Simple Crypto write up

## Challenge
Just as practice, we are given the following code:
```python
import sys
import random

key = sys.argv[1]
flag = '**CENSORED**'

assert len(key) == 13
assert max([ord(char) for char in key]) < 128
assert max([ord(char) for char in flag]) < 128

message = flag + "|" + key

encrypted = chr(random.randint(0, 128))

for i in range(0, len(message)):
  encrypted += chr((ord(message[i]) + ord(key[i % len(key)]) + ord(encrypted[i])) % 128)
```

as well as the following output:
```7c153a474b6a2d3f7d3f7328703e6c2d243a083e2e773c45547748667c1511333f4f745e```

## Solving

Most people solved it with Z3 but I took my own road less travelled. Basically we know that the first byte of the encrypted string is the "seed". We also know the format of the flag and we know that the key encrypts itself, i.e. the last 13 bytes are the encoded key byte. The script below solves it:

```python
import sys
import random
import os
import string

flag = 'TWCTF{'
output = '7c153a474b6a2d3f7d3f7328703e6c2d243a083e2e773c45547748667c1511333f4f745e'

## Decrypt the output to bytes and set it up
orstr = output.decode('hex')
key_enc = orstr[-13:]
messi = orstr[1:len(orstr)-13-1]
weirch = orstr[len(orstr)-13-1:len(orstr)-13]
pos_wc = len(orstr)-13-1
seed = orstr[0]

keyer = ''

for i in range(0,len(flag)):
    tmp = messi[i]
    fli = flag[i]
    for j in range(128):
        if (j + ord(fli) + ord(seed)) % 128 == ord(tmp):
            print chr(j)
            keyer +=chr(j)
            break
    seed = messi[i]

## simple encryption based on the original but smaller
def enc(msg,key):
    seed = '|'
    for i in range(0, len(msg)):
        seed += chr((ord(msg[i]) + ord(key[i % len(key)]) + ord(seed[i])) % 128)
    return seed.encode('hex')

## simple decryption
def dec(msg,key):
    magi = ''
    seed = msg[0]
    try:
        for i in range(1,len(msg)-1):
            ju =  (ord(msg[i]) - ord(seed) - ord(key[(i-1)%len(key)]))
            while ju < 0:
                ju += 128
##            print chr(ju)
            seed = msg[i]
            magi+=chr(ju)
    except Exception as e:
        return magi
    return magi

## Always set up your printable chars!
printi = string.ascii_letters + string.digits + '{}_|!?^-'

def ispri(s):
    for j in s:
        if j not in printi:
            return False
    return True


## Second part of bruteforcing
def keylongerer(i,target, key, stri):
    for i in range(i):
        checker = dec(stri,key+'\00'*(13-len(key)))[-(13-len(key)):]
        tmp = ''
        for i in checker[1:]:
            if i in printi:
                tmp+=i
        print "possible key: %s" % key + tmp
        key = key + tmp
        
    if len(key) < target:
        print "Warning, key length is only %s (missing %i), consider expanding the set or bruteforcing" % (str(len(key)),target-len(key))
    print dec(stri,key+'\00'*(13-len(key)))
    return key
keyer = keylongerer(10,13,keyer,orstr)

## Third and last part of bruteforcing
for j in range(128):
    tk = keyer + chr(j)
    if ispri(dec(orstr,tk)):
        if dec(orstr,tk)[len(dec(orstr,tk))-len(keyer):] == keyer:
            print tk
            print dec(orstr,tk)

```
It's a 3-stage brutefrocing: the flag format 'TJCTF{' allows us to find out the first 6 chars of the key. The keylongerer makes the name longer (as the name indicates) and finally the last bit finds the last char. This last bit can be repeated if, say, 2 chars are missing. It's super fast....

Flag is: ```TWCTF{Crypto-is-fun!}|ENJ0YHOLIDAY!```
