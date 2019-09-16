from utils import socki
from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes
import signal
import time
import gmpy2
import random
from fractions import gcd
##from FaultOrig import RSA
from RSASolver import *


e=0x10001

def n2s(n):
    return long_to_bytes(n).decode('latin-1')

pow2 = 2**e
pow3 = 3**e
t = time.time()
s = socki('crypto.chal.csaw.io 8081')
t0 = time.time()


def gen_prime():
    base = random.getrandbits(1024)
    off = 0
    while True:
        if gmpy2.is_prime(base + off):
            break
        off += 1
    p = base + off

    return p

def s2n(s):
    return bytes_to_long(bytearray(s, 'latin-1'))

s.recv(1024)


def encrypt(m,n):
    return pow(m,0x10001,n)


def exEnc(m,n):
    return b'%X\n' % encrypt(s2n(m),n)

##
##
##def checkN(t,m):
##    for i in range(0,100000):
##        if i%100 == 0:
##            print i
##        random.seed(round(t - i/100000.0,5))
##        p = gen_prime()
##        q = gen_prime()
##        n = p*q
##        if exEnc(mimi,n) == m:
##            print p,q
##    

def getRealFlag():
    s.send('1\n')
    time.sleep(0.8)
    return s.recv(4096).split()[0]

def getFakeFlag():
    s.send('2\n')
    time.sleep(0.8)
    return s.recv(4096).split()[0]

def getFakeFlagCRT():
    s.send('3\n')
    time.sleep(0.8)
    return s.recv(4096).split()[0]
    
def getFlagRemote(n):
    fake_flag = 'fake_flag{%s}' % (('%X' % n).rjust(32, '0'))
    s.send('4\n')
    time.sleep(0.8)
    s.recv(1024)
    s.send(fake_flag + '\n')
    time.sleep(0.8)
    return s.recv(4096).split()[0]

def getFlagLocal(i,n):
    s = 'fake_flag{%s}' % (('%X' % i).rjust(32, '0'))
    return pow(s2n(s),e,n)


def getEncrypted(n):
    s.send('4\n')
    time.sleep(0.8)
    s.recv(1024)
    s.send(n + '\n')
    time.sleep(0.8)
    return int(s.recv(4096).split()[0],16)
    
two = getEncrypted('\x02')
three = getEncrypted('\x03')
four = getEncrypted('\x04')
nine = getEncrypted('\x09')

print 'calcs'
n_1 = gcd(pow2-two,pow3-three)

assert pow(2,e,n_1) == two

ff1 = int(getFakeFlag(),16)
ff2 = int(getFakeFlagCRT(),16)
rf = int(getRealFlag(),16)

def retrieveX():
    for i in range(1000000):
        if getFlagLocal(i,n_1) == ff1:
            return i

def checkEnc(i,n):
    s = 'fake_flag{%s}' % (('%X' % i).rjust(32, '0'))
    return pow(s2n(s),e,n)
    

p = retrieveX()

actual_fake_flag = 'fake_flag{%s}' % (('%X' % p).rjust(32, '0'))

##for i in range(1,1000):
##    if n_1%i == 0:
##        n_1 = n_1/i

assert checkEnc(p,n_1) == ff1

p = gcd(pow(s2n(actual_fake_flag), e, n_1)-ff2, n_1)

q = n_1 //p

print solve(p,q,e,c)
