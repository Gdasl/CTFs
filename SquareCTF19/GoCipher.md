# Go Cipher

A fun challenge. We essentially get a go script as well as binaries for different OS and 11 files: 5 pairs of plaintext/ciphertext and 1 encrypted flag. The goal is to decrypt the flag (duh!)

Here is the go script (extract):

```go
func encrypt(plaintext []byte, key []byte) string {
  x := uint64(binary.LittleEndian.Uint64(key[0:]))
  y := uint64(binary.LittleEndian.Uint64(key[8:]))
  z := uint64(binary.LittleEndian.Uint64(key[16:]))

  keyid := md5.Sum(key)
  r := keyid[:]
  for _, e := range plaintext {
    t := (e - byte(x)) ^ byte(y) ^ byte(z)
    r = append(r, t)
    x = bits.RotateLeft64(x, -1)
    y = bits.RotateLeft64(y, 1)
    z = bits.RotateLeft64(z, 1)
  }
  return hex.EncodeToString(r)
}
```

So pretty easy, first take a key, 24 bytes, and calculate the md5. That's the initial ciphertext block. Then split the key in 3 8 bytes (64 bit) segments and saves them as binary using little endian (i.e., "reversed"). Each character in the plaintext is then encrypted essentially using simple ```xor```. After each iteration the bit vectors are rotated.  The ```rotateLeft``` is a WYSIWYG function: it takes the rightmost bit and appends it to bitstring, repeating that procedure n times. Also worth noting that ```RotateLeft(a,n)``` == ```RotateRight(a,-n)```. 

### Solving: first attempt

OK so basically, what we see is that we have three unknown int64 (64 bit BitVectors essentially) but if we know them, every single iteration is deterministic. It's essentially a linear system where we know ```e``` (plaintext char) and ```r``` (ciphertext char). The generalized equation for any position ```i``` is thus:

```
(ord(plain[i])-(Byte(RotateRight(x,i%64))))^Byte(RotateLeft(y,i%64))^Byte(RotateLeft(z,i%64)) == ord(cipher[i])
```
Now we can easily find a key that could be valid, though there are many, which is why there is the md5 check. I first spent a number of time trying to find a key that would also checksum to the correct md5 for the first plain/cipher pair. The idea was that maybe, the right keys for each of the 5 pairs would give a hint about the key for the flag.

After running it for a few hours for both the first and second plain/cipher pair and warming up the atmosphere by a few degrees on account of my CPU (this is a laptop...), I realized it wasn;t the right way to go. Even if my solver found two correct keys per ms it was still too slow.


### Solving: second attempt
OK, new game plan. I went  back to the drawing board. I thought about the first solver. I essentially used the ```encrypt``` function to find the key. So why not use the ```decrypt```? The idea was simple: we know our plaintext, unlike our ciphertext, is printable. So we already drastically reduce the searchspace. While we introduce an additional ```n = len(ciphertext)``` variables, the much smaller search space for those might make it feasible. Not only that, but we know the flag format.

I wrote a new solver essentially doing the opposite of the first one and introducing the plaintext chars as variables. As a constraint I limited the value to under 127 (learned the hard way ```z3``` has special operations for unsigned integer comparison, which you need when working with BitVecs). Then I tried to add more constraints incrementally: the first char to ```f```, second to ```l```, third to ```a```. Boom, unsat. 

At this point I got a tea and it hit me, that the flag might not be at the beginning. So I looped over the position and checked if there exists a satisfiable model where
```pt[i] == 'f' or 'F'
pt[i] == 'l' or 'L'
pt[i] == 'a' or 'A'
pt[i] == 'g' or 'G'
```

Paydirt! Offset 17 is where it's at. From there it was relatively easy since I could add constraints making some educated guesses until it printed the flag. The final script takes half a second to find the flag.

