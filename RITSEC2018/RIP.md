# RIP.md

>+[----->+++<]>+.++++++++++++..----.+++.+[-->+<]>.-----------..++[--->++<]>+...---[++>---<]>.--[----->++<]>+.----------.++++++.-.+.+[->+++<]>.+++.[->+++<]>-.--[--->+<]>-.++++++++++++.--.+++[->+++++<]>-.++[--->++<]>+.-[->+++<]>-.--[--->+<]>-.++[->+++<]>+.+++++.++[->+++<]>+.----[->++<]>.[-->+<]>++.+++++++++.--[------>+<]>.--[-->+++<]>--.+++++++++++++.----------.>--[----->+<]>.-.>-[--->+<]>--.++++.---------.-.

Attached was a png image with weird borders.

## Identifying the challenge

The description is plain vanilla brianfuck and translates to a youtube url: [link](https://www.youtube.com/watch?v=F6LYOfeSWNM). It's a music video for "We are family" by Sister Sledge. Therein was the hint: look at the edges. And in fact the image had a weird border made up by a bunch of colors which didn't look random. I actually recognized it relatively fast as [piet](https://esolangs.org/wiki/Piet), which I had come accross while researching  What_Th.Fgck. 

## Solving

From there it was pretty straight forward: extract the border 1 color at the time, starting on the upper left corner and going clockwise, saving a new image whereby each pixel represents one square of the original border and feed it into an [online intrepreter](https://gabriellesc.github.io/piet/). EzPz
