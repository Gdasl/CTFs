# Broken GPS

>Ella is following a broken GPS. The GPS tells her to move in the opposite direction than the one she should be travelling in to get to her destination, and she follows her GPS exactly. For instance, every time she is supposed to move west, the GPS tells her to move east and she does so. Eventually she ends up in a totally different place than her intended location. What is the shortest distance between these two points? Assume that she moves one unit every time a direction is specified. For instance, if the GPS tells her to move "north," she moves one unit north. If the GPS tells her to move "northwest," then she moves one unit north and one unit west.

Input format:
>You will receive a text file with N directions provided to her by the GPS (the ones that she will be following) (1<=N<=1000). The first line in the file will be N, and each consequent line will contain a single direction: “north,” “south,” “east,” “west,” “northwest,” “northeast,” “southwest,” or “southeast.”

Output format:
>Round your answer to the nearest whole number and then divide by 26. Discard the quotient (mod 26). Each possible remainder corresponds to a letter in the alphabet. (0=a, 1=b… 25=z).

>Find the letter for each test case and string them together. The result is the flag. (For instance, a, b, c becomes “abc”). Remember to use the flag format and keep all letters lowercase!

## Solution

This was very straightforward. Essentially, Ella's movements are mirrored symetrically i.e. she will end up at (-x,-y) from her original destination and the distance will simply be ```2*sqrt(x**2+y**2)```, a simplified shortest distance formula. The script outputs the correct answer.

```
from math import sqrt

#smolstep = sqrt(2)/2
smolstep = 1

def read(f):
    pos = (0,0)
    pos2 = (0,0)
    
    g = open(f).read()
    g = g.split('\n')
    g = [i for i in g if i != '']
    k = [i for i in g[1:]]
    for i in k:
        pos = simpleParse(i,pos)
        
    return chr(97+int(round(simpleDistance(pos)))%26)

    
def simpleParse(di,pos):
    x,y = pos
    if 'north' in di:
        y += 1
    if 'east' in di:
        x += 1
    if 'south' in di:
        y -= 1
    if 'west' in di:
        x -= 1
    return (x,y)


def simpleDistance(pos):
    return 2*sqrt((pos[0]**2 + pos[1]**2))

print ''.join([read('%d.txt'%i) for i in range(1,13)]) 
```
