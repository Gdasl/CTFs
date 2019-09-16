# FaultBox (400)

> who's fault?? nc crypto.chal.csaw.io 1001
[server.py]

## Intro

At first glance we see this is this year's RSA challenge. It was actually quite interesting to do, the TLDR is that it was a fault attack on RSA signature. Funny enough (not), I managed to get the breakthrough at 19:59:50 UTC, narrowly missing the deadline...

## Anaylsing the code

We essentially have a service that allows us to do 4 different things:

1. Show the encrypted flag
2. Show the encrypted fake flag
3. Show the CRT-encrypted fake flag
4. Arbitrarily encrypt some text

I like to live by Chekhov's principle: if there's a gun on stage during act 1, you better be ready to use it during act 4. In other words, anything you get in a challenge should be useful. I thus set off to find flaws in the different options, starting with the obvious: prime generation.

### Prime generation and the pitfalls of floats

Here is the code to generate primes:
```
def gen_prime():
    base = random.getrandbits(1024)
    off = 0
    while True:
        if gmpy2.is_prime(base + off):
            break
        off += 1
    p = base + off

    return p, off
 ```
 
 Now the ```random``` is seeded using ```time.time()```. My first thought was to bruteforce the seed since we know when we connect to the server. My windows machine uses 3 precision decimals for ```time``` and thus my local tests actually worked and I was able to recover the correct primes in a few seconds. Now here is the thing: precision varies according to system: on linux, it's much higher. Long story short, a float can't be bruteforced and that's the story of how I lost a good few hours. 
 
 ### Fault attacks and why you should double-check your signatures
 
While on Discord, someone pointed out to google "fault attacks". So I did and it led me to [this](https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-4/). The issue arises when we have a faulty signature process during the partial calculation of either ```c_p``` or ```c_q```. When that happens, ```c**e - m``` will be a multiple of either only ```p``` or ```q```. Which means that ```gcd(c**e - m,n)``` will result in the non-faulty factor! So could this be it? Well let's have a look at the ```TEST_CRT_encrypt``` function:

```
def TEST_CRT_encrypt(self, p, fun=0):
        ep = inverse(self.d, self.p-1)
        eq = inverse(self.d, self.q-1)
        qinv = inverse(self.q, self.p)
        c1 = pow(p, ep, self.p)
        c2 = pow(p, eq, self.q) ^ fun
        h = (qinv * (c1 - c2)) % self.p
        c = c2 + h*self.q
        return c
 ```
 
 The ```fun``` parameter actually introduced an optional error factor for ```c_2```! As soon as it's not 0, the encryption will be faulty.

Great, so what do we need? It's easy: ```m```, ```c_faulty```, and of course ```n```. The only one we have is ```c_faulty```, as outlined above. Now let's get the rest.



#### Getting n

I racked my brain around that until I got a tip to have a closer look at the oracle. I started googling aruond until, lo and behold, I found [this](https://crypto.stackexchange.com/questions/65965/determine-rsa-modulus-from-encryption-oracle). You can essentially always get ```n``` if you have access to an oracle, by calculating ```gcd(2**e - E(2), 3**e - E(3)```. Sometimes this will result in a multiple of n but we can easily check that since it will mostly be by some small facotr (so just bruteforce...).

#### Getting m

We know the format of the ```fake_flag```:

```python
fake_flag = 'fake_flag{%s}' % (('%X' % y).rjust(32, '0'))
```

Where ```y``` is some ```int```, more often than not under 1000. Well, we can request the correctly encrypted ```fake_flag``` from the service, then bruteforce ```y```, encoding the resulting flag with our newly found ```n``` and check when they match!

### Solving

Ohyeahitsallcoimingtogether.gif. All we need to do now is to calculate one factor of n:

```python
p = gcd(pow(s2n(actual_fake_flag), e, n_1)-faulty_fake_flag, n_1)
```

Once we have this, it's trivial to calculate ```q``` and decrypt our flag!


 
 
 


