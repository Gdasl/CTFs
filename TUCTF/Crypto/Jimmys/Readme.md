# Jimmy's Crypto

> Your nemesis, we'll call him Jimmy for brevity's sake, believes that he has finally outsmarted you in his secret messaging techniques.
He's so confident that he even gave his source code.

>Show him where he went wrong!

## The source code

We get the code that jimmy used. At first glance it's pretty unbreakable and also equally useless: take two strings, get the length of the longest, create a random key of that length and xor both messages with that key. The script uses ```random.randint(0,256)``` to select random chars. 

At first glance this is pretty much unbreakable. I first thought there might be an angle to exploit in the PRNG. However, while ```random``` is highly unrecommended for cryptography, the default seed being the system time, it still remains too unpredicatble. So there had to be another, better way.

## Xoring using the same key - why it's a bad idea

Since xor is reversible, this is what happens:

```ciphertext1 = key ^ flag```
```ciphertext2 = key ^ message```

Therefore

```ciphertext2 ^ ciphertext1 = key ^ message ^ key ^ flag = message ^ flag```

Now this means that the result of xoring the two ciphertext only yields characters that result when two printable characters are xored. Exploiting this property, we can perform a so-called cribdrag anaylsis.

## Crib-dragging

I used [this repo](https://github.com/SpiderLabs/cribdrag). I knew ```TUCTF{``` was in the flag which showed me ```teal m``` in the secret. From there I worked my way back and ultimately got the flag!
