# Hardshells

>After a recent hack, a laptop was seized and subsequently analyzed. The victim of the hack? An innocent mexican restaurant. During the investigation they found this suspicous file. Can you find any evidence that the owner of this laptop is the culprit?

## The setup
We get a zipfile which is password protected. This part actually took me the longest: I couldn't figure out the password and didn't even try to fcrack it. I left the challenge and came back to it after a a day or two and instantly realized it had to be tacos ('hardshells' had to be a hint). This correctly unzipped a nice file.

## The weird file
The complete file was about 5M in size but opening it with hexedit quickly revealed it to be mostly null bytes. The only exception were a few snippets here and there and a huge snippet in the upper half which suspiciously reminded me of a PNG. Except for the header which said ```PUG``` instead of PNG. So I knew something was fishy.

## The solving - going round the world
Looking back, it was so easy. Most teams correctly identified the file as a Minix filesystem which could be mounted and that contained the PNG. Instead, I went the hard way. Which meant deleting everything before 'PNG' and everything after 'IEND', leaving me with a broken PNG file. I got a PNG but it only showed the top row, about 1/40 of the image, the rest was some dark mess.

Using PNG check it quickly showed me that there was something wring with the IDAT checksums and the IDAT length. Basically, a PNG is broken down in chunks and each chunk always has the following structure:

[Length = 4 bytes][Type = 4bytes][Data = Length bytes][CRC sum = 4 bytes]

The first IDAT's Length and checksum were all messed up. I first tried to change the length and manually repair the checksums. Took me forever and didn't lead anywhere. In the end, I realized that there was a chunk of null bytes in the middle of the first chunk which happened to have the exact size of [actual length - indicated length]. Removing that chunk and saving gave me the file and the flag.

Looking back, the way I took was absurdly complicated but I actually learned a ton about PNG which was super helpful (I was actually able to repair a few files IRL after this). Really liked the challenge, 10/10 would do again.


