# VeggieTales

> It's my favorite show to watch while practicing my python skills! I've seen episode 5 at least 13 times.

## The problem

We were only provided with a nc link, no executable. That's already a red flag right there. Who doesn't provide a binary ?!. But fine, let's see. Connecting shows us a simple text interface revolving around veggie tales episodes where we can:
- list episodes
- add episodes to the watched list
- backup our list
- load a backup

Providing a way to load stuff is very rarely a good idea unless you know exactly what you are doing. I knew right ways this had to be the exploit. Printing the backup looked like a straight forward b64 encoded string which you could also upload so I figured this was going to be straightforward.

## The solving

Turns out decoding the b64 gave junk. Ok, that's fine, it's probably compressed. Pickle was my first idea (before even seing the hint) but pickle doesn't garble strings, it's still recognizable, even when you try to wrap complex structures. I tried implementing Episodes as a class, then watchlist as a class of classes but still, nothhing worked. I tried various compression algorithms but all failed.

The hint mentioned 13. This should always be an immediate red flag pointing to rot13. I tried that early on but no dice, rot13 the bytes of the decoded base64 also yielded junk. And then I tried to do the obvious: rot13 the base64. And behold, a valid pickle3 pickle!

Following this it was pretty easy. Googling around you'll find [this link](http://anthonyvoza.blogspot.com/2018/11/rootme-ctf-app-security-python-pickle.html) which explains the pickle exploit at lenght. From there it was a simple matter of adapting the script, converting the resulting pickle to base64, rot13 that and upload it to the server. Easypeasy.

