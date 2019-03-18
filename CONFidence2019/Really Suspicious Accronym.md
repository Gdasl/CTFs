# Really Suspicious Accronym

> You can't break my public key if you don't know it, amirite?

# The premise

We get an output file as well as the generator script. This is obviously RSA so this will probably be a factorization problem. Upon opening the file however, we see that there is no N. Rather, N is generated and 3 messages are encrypted, of which 2 are known. The messages spell out ```You can't factor the modulus If you don't know the modulus!```. So the challenge was 2 parts: 1) find out n, 2) factor n

# The solving

## Finding n
We know that rsa encrypts a cipher as follows:```c = m^e % n```. This is akin to say: ```m^e = c + k*N``` where k is an integer. As such, if we take the GCD of ```m1^e - c1``` and ```m2^2 - c2``` we will get N.

## Factoring N

So now that we have N we need to factor it. Looking at the prime generation we see it's kind of fucky.

```python
tmp = randint(2**1023, 2**1024)
e = 65537
p = next_prime(0xDEAD*tmp+randint(2, 2**500))
q = next_prime(0xBEEF*tmp+randint(2, 2**500))
```

That implies:

```
n = (0xDEAD*tmp+A) * (0xBEEF*tmp+B)
n = (0xDEAD*0xBEEF*tmp^2 + 0xBEEF*A*tmp + 0xDEAD*B*tmp + A*B)
```
```tmp^2``` is obviously the heavy hitter here. So we can make an educated approximation that ```p=sqrt(N/(0xDEAD*OxBEEF))``` This reeks of coppersmith. It actually is and we can use an exisitng script to solve it. We simply assume ```q = p*0xBEEF - 2**500``` the  plug it in the nifty script and promptly comes the flag.

```python
fact = 0xdead*0xbeef

p_approx = isqrt(N/fact)
q_approx = 0xbeef*p_approx - 2**500

F.<x> = PolynomialRing(Zmod(N), implementation='NTL')
f = x - q_approx

roots = f.small_roots(X=2**500, beta=0.1)
for delta in roots:
    print('delta', delta)
    print('q_approx - delta', q_approx-delta)
    q = q_approx-delta
    p = int(N)/int(q)
    d = inverse_mod(65537, (p-1)*(q-1))
    print("d", d)
    decrypted = hex(int(pow(c,d,N)))
    print decrypted[2:-1].decode('hex')
````
