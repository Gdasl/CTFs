# SuperCurve (300)

>We are a super legitimate crypto company asking you to complete an audit on our new elliptic curve, SuperCurve, in order to show those hecklers at WhiteHat how legit we are! nc crypto.chal.csaw.io 1000

### Intro

This got my hopes up, only to dash them: it looks like a nice ECC challenge where we need to find the secret. However, it turned out to be a simple bruteforcing challenge, whether by bad luck or by design... Essentially the order of the curve is very, very, very, very, very low. Like absurdly low. It took around 2s on my machine. Still, not one to spit on 300 freebies.

### Analyzing the code

As said, it's pretty straightforward: we get 2 files, one is a server and one is a simple ECC implementation. The server simply creates a curve, gets a random int within the bounds of the order, multiplies that point with the curve and displays the result. Our task is to find the secret scalar. Code:

```python
    secret_scalar = random.randrange(curve.order)
    base = curve.g
    pub = curve.mult(secret_scalar, base)
    print("Public key: {}".format(pub))
    print("Secret scalar: {}".format(secret_scalar))
    ```
    
### Solving

Here's the thing about low orders: they limit your possibilities. Not only that but combined with fixed parameters, as we had here, and you're about as secure as a cheeto in lieu of a door bar. And that's exactly what was done here. The curve parameters are hard-coded:

```python
curve = SuperCurve(
    field = 14753, order = 14660,
    a = 1, b = -1, g = (1, 1),
)
```

So basically we can precompute all ```[secret_scalar,pub]``` pairs as a dic and look up whatever the server sends us. 7ez9me.



