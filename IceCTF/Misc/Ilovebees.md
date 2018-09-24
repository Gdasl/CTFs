# Ilovebees

>I stumbled on to this strange website. It seems like a website made by a flower enthusiast, but it appears to have been taken over by someone... or something.
Can you figure out what it's trying to tell us?
https://static.icec.tf/iloveflowers/

## The setup

Tone took me longer than I would have wanted. The website is a mess, there is a countdown stemming from some simple javascript. It counts down until sometime in 2025. There are also a bunch of broken links and the source code is an absolute disaster. Googling a bit, you end up on a very similar website, called I love flowers, which was actually a guerilla marketing campaign of sort for Halo back in the 2000s. Reading up on it, there are several mentions of steganography which leads to think there might be something hidden in the pictures.

## The solving

There are several pictures on the site: some jpgs and a couple of gifs. None reveal anything of the ordinary. That is until you look up and realize the favicon is also a gif. Strange. Downloading it and opening it in a hexeditor or running strings on it reveals a bunch of strange names like libc and stuff that just looks out of place. 

Saving as PNG yields 109 individual frames. Opening the first in hex editor we get something very familiar in the first PLTE chunk: 'ELF'. Could it be? I wrote the following quick and dirty script:

```python
import png

arr = []
for i in range(110):
    tmp = 'favicon1-'+str(i)+'.png'
    im = png.Reader(tmp)

    for c in im.chunks():
        if c[0] == 'PLTE':
            arr.append(c[1])
            
f = open('new','wb')
f.write(''.join(arr))
```

It gives us a nice ELF. It probably prints out the flag but that would have been overkill since the flag is actually stored inside as a string. And done.
