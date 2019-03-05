# RSAaaay

>Hey, you're a hacker, right? I think I am too, look at what I made!

>(2531257, 43)

>My super secret message: 906851 991083 1780304 2380434 438490 356019 921472 822283 817856 556932 2102538 2501908 2211404 991083 1562919 38268

>Problem is, I don't remember how to decrypt it... could you help me out?

## Solving

This was also easy, we are given a very small ```p``` and ```e```. The former is easily factored ```2531257 = 509 × 4973```. Now all we need to do is apply basic steps of calculating ```d = modinv(e,phi)``` where ```phi = (p-1) x (q-1)```.

The trick here was to quickly see that the message had spaces for a reason. Basically, up to 2 chars were encoded at a time. You could then simply convert to chr and read the flag.
