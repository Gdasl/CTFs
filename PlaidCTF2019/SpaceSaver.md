# Space saver

## The Problem
We get a simple dd file which is essentially an image container, uncompressed. Examining with binwalk reveals there are 4 images (PNG) as well as one rar file. I tried extracting but it would throw an error so I manually extracted directly from the hex dump into 4 new files. 3 of the images are those of a lock, 1 is something that looks like the solution but with no flag.

The rar itself is proteccted. Running john and rockyou on it for 30min didn't yield anything so it was safe to assume the password was somewhere in the files. Unfortunately, time ran out by that point and I coulnd't complete the challenge.

## The Solving
It turns out that looking again at the original dump, there is something written after the ```IEND``` marker of the locks images. The 3 strings are ```Spac```, ```3ei2``` and ```herE```. Concatening those forms the password that ultimately unlocks the rar and reveals the flag image.
