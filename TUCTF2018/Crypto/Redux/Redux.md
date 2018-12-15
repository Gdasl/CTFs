# Never Ending Crypto Redux

>The challenge is back and stronger than ever!
IT WILL NEVER END!!

>Good luck. You're gonna need it.

>nc 18.223.156.26 12345

## First steps

No source code, only an address. This doesn't bode well. Basically, the script first asks for input, encrypts it and sends it back. We are also greeted by an ominous "Level 0" hinting there might be more (SPOILER ALERT: there are). So I went level by level until the end.

## Owning this

Note: all levels start with dots and dashes, i.e. morse or a variation thereof.
### Level 0

Plain morse. Simply decrypt and send. Easy peasy.

### Level 1

Morse, than rot13. Also easy.

### Level 2

This was morse but the dots are dashes and vice versa. I called it MorseInv.

### Level 3

So level 3 is where my shame begins. I failed to identify the cipher. I knew it was transposition but my attemps and identifying the correct one failed miserably. At this point it was also around 2 am and I was pretty exhausted. I went to sleep and went directly back to it upon waking up. I resolved to do it the ugly way: bruteforcing. Using a mix of ciphers and some actualy hardcoded transposition functions i built a functiion that will decrypt anything between 5-15 chars. I called it bruteDecrypt. But it did the trick and as mom says, if it's stupid and it works, it ain't stupid!

### Level 4

The string was first decrypted using bruteDecrypt then rot13. So combination of level 1 and 3 Buum done.

### Level 5

Same as level 4 but the morse is inversed and rot13 (level 2 + level 3 + level 1)

### Level 6

This one also took me a while. I couldn't recognize Vigener (which is what it was), but recognized that the letters were shifted by fixed amounts depending on their position in the string. So I simply hardcoded that up to length = 15. Buum, ugly but donezo.

### Final level: Level 7

Ah, the fun of 7. This took me a while as well and I ended up encrypting a bunch of strings using my own strings to get the right combination since it was obviously a mix of previously used ciphers, keeping in line with the previous levels (at least I hoped so). Turns out it's simply inverse morse, transposed, run through a vigenere cipher, albeit a different one then for level 6. So level 2 + level 3 + level 6.

## Final words

The challenge took me roughly 4h to compete but was fun to do since I love scripting stuff, one of my favorite ones in the competition!
