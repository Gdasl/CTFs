# Revolutional Secure Angou

## Task
This task had us receive a 3 files: a key.pem, an ecrypted flag and a ruby script. We can quickly see that this is avery crude RSA implementation using Ruby SSL' BigNum. Extracting the key gives us ```e = 65537```and a 2048-bit modulus. I quickly tried a few basic things (factordb, ROCA vuln, fermat) and relatively soon realized all this being secure, it had to be some prime-generation weakness.

## The Weakness

Taking a closer look at the ruby script:

```ruby
require 'openssl'

e = 65537
while true
  p = OpenSSL::BN.generate_prime(1024, false)
  q = OpenSSL::BN.new(e).mod_inverse(p)
  next unless q.prime?
  key = OpenSSL::PKey::RSA.new
  key.set_key(p.to_i * q.to_i, e, nil)
  File.write('publickey.pem', key.to_pem)
  File.binwrite('flag.encrypted', key.public_encrypt(File.binread('flag')))
  break
end
```

We see that while p is generated randomly, q is generated based on p. More exactly, q is generated so that ```q * e % p == 1```. THis is as fishy as it gets, you should never, under any circumstance, generate primes that way. 

## The Solving

From here on it's a walk in the park. Using a bit of modular arithmetic:
```
q * e % p = 1
(q*e) - 1 = p*j
p = ((q*e)-1)/j
```
where j is an integer and j < e. Now since ```n = p * q```:
```
n = ((q*e)-1)/j * q
n*j = e*q^2 - q
e*q^2 - q - n*j = 0
```
The last is just a simple quadratic equation. All we need to do now is to solve it for 0 < j < 65537, check if the solution is prime, and check if the solution is a divisor of n. On a decent i7 using sympy it takes around 10 seconds / 1000 (7000 if you parallelize), whic makes bruteforcing a very convenient way of solving this.


