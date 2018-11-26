from PIL import Image
import numpy as np

arr = ['blue%d.png' % i for i in range(1,8)]

im = Image.open('CheckOutThisFilter.png')


aa = im.getdata()
b = []

for i in aa:
    b.append(bin(i[2])[2:])


def channel(img, n):
    """Isolate the nth channel from the image.

       n = 0: red, 1: green, 2: blue
    """
    a = np.array(img)
    a[:,:,(n!=0, n!=1, n!=2)] *= 0
    return Image.fromarray(a)
