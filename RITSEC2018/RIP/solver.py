from PIL import Image
import numpy as np
import scipy.misc as smp

a = Image.open('RIP.png')

w,h = a.size

arr = []
for i in range(0,w,10):
    tmp = a.getpixel((i,5))
    arr.append(tmp)

print len(arr)

for i in range(10,h,10):
    tmp = a.getpixel((905,i))
    arr.append(tmp)

tmparr = []
for i in range(0,w-10,10):
    tmp = a.getpixel((i,905))
    tmparr.append(tmp)

arr.extend(tmparr[::-1])

tmparr = []
for i in range(10,h-10,10):
    tmp = a.getpixel((5,i))
    tmparr.append(tmp)


arr.extend(tmparr[::-1])

data = np.zeros( (360,1,4), dtype=np.uint8 )

bubu = 0
for i in range(360):
    data[i,0] = arr[i]
                  


