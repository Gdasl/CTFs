# Hydra

This was a MISC forensics challenge. It actually looked pretty straight forward: we get a single ```png``` image. Opening the file with a hex editor we see there are a bunch of other files in there as well as several red herrings. Among those there are several archives, all ultimately containing a simple ```flag.txt``` file with the text "Looking for flag".

One of the non-archive files was a simple png, a screenshot of a MsgBox. I tried to extract LSB, decode the zlib stream manually but I didn't think to check the EXIF data.... Turns out checking it reveals a copyright notice:

```frps{Fj0eqs15u_sy4t_u1qq3a_1a_z3g4}```


Running it through a caesar cipher bruteforcer yields the flag:

```secf{Sw0rdf15h_fl4g_h1dd3n_1n_m3t4}```
