from supercurve import SuperCurve, curve
from utils import socki
import time

def go():
    curve = SuperCurve(
        field = 14753, order = 14660,
        a = 1, b = -1, g = (1, 1),
    )

    d = {}
    d2 = {}
    base = curve.g
    for i in range(curve.order):
        pub = curve.mult(i, base)
        d[pub] = i
        d2[i] = pub
    return d,d2
        

dpub,di = go()
s = socki('crypto.chal.csaw.io 1000')
time.sleep(1)
print s.recv(1024)
