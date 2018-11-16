# Shredded

> Instructions to disable C3 were mistaken for an advertisement for new housing on Charvis 9HD. They’ve been shredded in the final office tidy-up. Nobody bothered to empty the trash, so a bit of glue and you should be good?

The challenge was very similar to one in the NightHawk CTF practice round. Basically you take a picture, divide it up in equally sized slices and shuffle them. There are several algorithms out there which can reconstruct such an image based on ressemblance index (i.e. how similar is one column to another). 

The rub here was that it's obviously a QR v.1 code which are a) small b) not necessarily deterministically built (the fact that 2 columns are similar matters little in a QR code). So this was ultimately a intuition meets brute force exercise.

## Solving

The premise was that a QR code always has 3 squares used for the calibaration: one on each corner but the right-bottom one. Moreover, there are no completely white columns in a QR code. I started scripting the identification of left and right corner as well as middle but quickly realized that given the number of fragments (22 once you removed the whites), it would be faster by eye.

I ended up with the following:


3 slices for left coreners (order unknown)
2 slices immediately adjacent to those corners (side unknown)
2 slice addjacent to the 2 previous ones (side unknown)
1 slice separating the left corner from the middle (known position: 8th from left)
6 slices for middle
1 slice separating middle from right corner (known position)
5 slices for right corner, following the logic above.

All I needed was:

1) combine all possible solutions

2) save each as image

3) read in using zbar

4) check if valid QR code.

The bruteforcing took about 30 seconds and promptly yielded the code. It's ugly and could be optimized but the improved efficiency was negligible in relation to the effort needed.
