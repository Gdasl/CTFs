# ConverRSAtion

## Challenge

```
Alice and Bob were communicating over an insecure channel. Eve was listening on the whole conversation and this is what she saw:

Alice: Should I send you the flag?
Bob: Fine. But make sure you encrypt it.
Alice: That's a given. But first let me send you an encrypted test message.
Alice: test_ciphertext.txt
Bob: Well, everything works just as expected. Just send the flag already.
Alice: Here you go.
Alice: ciphertext.txt
Given the limited information, Eve went to Bob's website to learn some more. She found that for different public exponents, Bob uses the same message space. Moreover, Eve found an implementation of the RSA cryptosystem in Bob's GitHub repository. From all the information Eve could gather, can you help her retrieve the flag?
```
Note: I learned about the CTF only after it was over and thought this could be a fun challenge since only one team solved it during. It was quite interesting and I learned a lot. 11/10 would do again.

## The RSA implementation

Let's start at the beginning. This is a classic case of RSA generation weakness and a solid lesson in why you shouldn't cut corners. Here is the implementation as given by the challenge:

```python
# Utility Functions

def to_bytes(n, length, endianess='big'):
    h = '%x' % n
    s = ('0'*(len(h) % 2) + h).zfill(length*2).decode('hex')
    return s if endianess == 'big' else s[::-1]

def string_to_int(str_):
    return int(str_.encode('hex'), 16)

def int_to_string(int_):
    return to_bytes(int_, int(math.ceil(int_.bit_length() / 8)), 'big')

# RSA Cryptosystem
class PublicKey(object):
    def __init__(self, n, e):
        self.n = n
        self.e = e
    
    def encrypt(self, pt):
        return power_mod(pt, self.e, self.n)

class PrivateKey(object):
    def __init__(self, d, pk):
        self.d = d
        self.pk = pk
    
    def decrypt(self, ct):
        return power_mod(ct.ct, self.d, self.pk.n)
    
class Ciphertext(object):
    def __init__(self, pk, message):
        self.pk = pk
        self.ct = pk.encrypt(message)
        
def generate_key_pair(K):
    p = get_prime(K/2)
    q = get_prime(K/2)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    d = p
    e = inverse_mod(d, phi_n)
    public_key = PublicKey(n, e)
    private_key = PrivateKey(d, public_key)
    return (public_key, private_key)

pk, sk = generate_key_pair(2048)
print("Key-Pair Generated.")

test_m = string_to_int('Test Message')
test_c = Ciphertext(pk, m)
```
The fishy part happens during the ```generate_key_pair```. Normally, in RSA, you chose 2 distinct prime of size N/2, obtain n by multiplying p and q. You then chose or calculate e, the public exponent, such that it is coprime to the totient of phi = (p-1) * (q-1). Usually 65537 is used, avoiding the need for this step. Finally, d, the private key, is calculated as the modular inverse of e and phi.

This implementation basically gets it all wrong. It starts by chosing a d that is equal to p (so a factor of n) and then uses that to generate e. A bit of modular math helps here:

```
e === 1 mod (p-1)
r^e = r mod p for any r
r^e mod n = (r mod p) mod n
```
We end up seeing that ```r^e − r mod n ``` has p as a factor, which allows us to write: ```p=gcd(n,r^e − r mod n)```

Ok so we have a way to find p but we still need n. How do we find it? Simple, the challenge mentions "message space". It took me a while to see it and actually had to resort to crypto stackexchange: the message space is defined as [1 : n) or in other words, the upper bound of the message space is n-1. I.e. n = message space + 1.

## Solving

At this point it becomes relatively easy: for each e we compute ```r^e − r mod n```(using the property ```(A + B) mod C = (A mod C + B mod C) mod C```), check the gcd of each value and n and check if we hit paydirt. Flag is then spit out.

Note: ```parse``` and ```decrypt``` are simple helper functions that I implemented in python, can be found anywhere or just coded yourself.

```python
from MillerRabion import *
from Arithmetic import *
from Crypto.PublicKey import RSA
from rsa import *
import math
from decryptRSA import *

f = open('pubexps.txt','r')
tester = int(open('testcipher.txt','r').read())
li_e = [int(i.strip('\n').split(' ')[1]) for i in f.readlines()]
m_sp = 6169889543272941774424894315899193178732206138045806404561237345082277449903413488080427481122467158099322125074758249773067516719313889615943787009408630706771500165645713897720456390653445179419106972079371353107023405870506244751759001029616243527130022520235737585145266511315625907957231671867714675258683951405681229612056743863942913725681105276156093968201289931664091828184824066626331996076989565135036048997459124667056226783842642930864290137996382588033963058016834196192729985299190638398158286884097980236515475334660992373008696017655787776803439438513681064555462452503812772006618974339123314045688
cipher = int(open('cipher.txt','r').read())
n = m_sp + 1
test_m = string_to_int('Test Message')

#r^e - r modn === (r^e mod n - r mod n) mod n

def evaluateE(li,n):
    li2 = []
    for i in li:
        li2.append((pow(2,i,n)-(2%n))%n)


    pot_p = []
    for i in li2:
        if gcd(i,n) > 12234:
            pot_p.append(gcd(i,n))
    if len(pot_p) == 1:
        p = pot_p[0]
        assert(miller_rabin(p))
        print "found a factor!\n"
        return p
    else:
        try:
            for i in pot_p:
                assert(miller_rabin(i))
            print  "found several possible factors\n"
        except Exception as e:
            print "Potential error, check individually\n"
        return pot_p
        
p = evaluateE(li_e,n)
print parse(decrypt(cipher,p,n))
```



