from utils import socki, transpose
import time
from problem import good_image, inverse_baking
from fractions import gcd


def getAll():
    s = socki('crypto.hsctf.com 8112')
    tmp = s.recv(2049)
    tmp = s.recv(2049)
    return tmp



tmp = []
for i in range(7):
    time.sleep(0.1)
    tmp.append(inverse_baking(eval(getAll())))


def gcdm(li):
    return reduce(lambda x,y:gcd(x,y),li)


print ''.join([chr(gcdm(i)) for i in transpose(tmp)])
