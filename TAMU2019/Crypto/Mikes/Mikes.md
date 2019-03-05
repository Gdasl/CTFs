# Mike's Marvelous Mystery Curves

>Mike, the System Administrator, thought it would be a good idea to implement his own Elliptic Curve Diffie Hellman key exchange using unnamed curves to use across the network. We managed to capture network traffic of the key exchange along with an encrypted file transfer. See if you can read the contents of that file.

>Note: The password to the AES192-CBC encrypted file is the shared key x and y coordinates from the key exchange concatenated together. (e.g. sharedKey = (12345,67890) password = "1234567890")

## The Problem

We got a single pcap file which promised some juicy keys. As in all ECC challenges, in order to solve we need the parameters of the curve (```n```,```A```,```B```), a generator point ```g``` and at least 2 points ```p1```, ```p2```. Once you have that it's extremely straightforward and anyone with access to cocalc can solve it using sage's builtin functions. The additional challenge here was to decrypt a file that was also included in the pcap and encrypted using AES-192 which key was the x,y coordinates corresponding to the private key.

## Solving

There were several steps. The most obivous one was finding the parameters. Scouring the pcap revealed 2 key exchanges as promised, recognizable thanks to the ```BEGIN CERTIFICATE``` and the usual base64 dump that followed. But no matter where I tried to decode it, the key wasn't recognized as valid. 

Again, this was MEAN. It turns out that this was simply text encoded as b64 and enclosed by common certificate tags. The way to go was to simply decrypt as b64 and you got the actual key...

Each key yielded an ```n```, ```A```,```B```, ```(g_x,gy)```, ```(Pi_x,Pi_y)```. After making sure that ```n```, ```A```,```B```, ```(g_x,gy)``` were identical for both keys it was just a matter of computing the curve and the inverse logarithm in order to find x and y for which there are enough sage scripts out there. Making sure that ```(x,y)``` were identical for both public keys confirmed that the values were correct. Moreover, knowing that the file was encrypted using AES-192 meant the key had to be 24 bytes long, which it was.

All that was left was to decrypt the file that was readily extractable using wireshark with the correct key. Voilà, dumpt of text with the flag in it!
