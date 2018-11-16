from PIL import Image
import base64
import os

li = []
for fn in os.listdir('.'):
	if 'png' in fn:
		li.append(fn)
##
##li2 = []
##fnl = []
##for fn in li:
##    tmp = Image.open(fn)
##    li2.append(tmp.getdata())
##    fnl.append(base64.decodestring(fn[:-4]))
##    tmp.close()
##
##
##
##li2 = []
##fnl = []
##for fn in li:
##    os.rename(fn,base64.decodestring(fn[:-4])+'.png')
##




##
##
##li2 = []
##fnl = []
##for fn in li:
##        if len(fn.split(' ')[1].split('.')[0]) == 1:
####                print fn
##                tmp = fn.split(' ')
##                os.rename(fn,tmp[0]+' 0'+tmp[1]+'.png')

def convertToBin(im):
        pixels = list(im.getdata())
        w,h = im.size
        pixels = [pixels[i * w:(i + 1) * w] for i in xrange(h)]
        arriMaster = []
        for i in pixels:
                tmp = []
                for j in i:
                        if j == (255,255,255):
                                tmp.append(1)
                        else:
                                tmp.append(0)
                arriMaster.append(tmp)
        return arriMaster


def identifyBorder(arr):
        zone1 = (33,43)
        zone2 = (49,87)
        zone3 = (93,109)
        zone4 = (187,197)
        zone5 = (203,241)
        zone6 = (247,263)
                
        

        
def assm(li,n):
        images = map(Image.open, li)
        widths, heights = zip(*(i.size for i in images))
        total_h = sum(heights)
        max_w = max(widths)
        new_im = Image.new('RGB', (max_w, total_h))
        y_offset = 0
        for im in images:
                new_im.paste(im, (0,y_offset))
                y_offset += im.size[1]
                new_im.save('test'+str(n)+'.jpg')
        for i in images:
                i.close()



def assm2(li):
        images = map(Image.open, li)
        widths, heights = zip(*(i.size for i in images))
        total_width = sum(widths)
        max_height = max(heights)

        new_im = Image.new('RGB', (total_width, max_height))

        x_offset = 0

        for im in images:
                new_im.paste(im, (x_offset,0))
                x_offset += im.size[0]
                new_im.save('test_fin.jpg')
        
