from socket import socket
from Morse import decrypt
from transFunc import *

import re
import random

def rot13(s):
    return ''.join([chr(ord(i)-13) for i in s])
    
host = '18.223.156.26'
port = 12345

s = socket()
s.connect((host, port))

def morse():
    new = ''
    while not 'Decrypt' in new:
        new = s.recv(1024)
##    print new
    r2 = re.compile("Decrypt (.*?)\n")
    deci = decrypt(r2.findall(new)[0])
##    print deci.lower()
    s.send(deci+'\n')

def morse13():
    new = ''
    while not 'Decrypt' in new:
        new = s.recv(1024)
##    print new
    r2 = re.compile("Decrypt (.*?)\n")
    deci = decrypt(r2.findall(new)[0])
    deci= deci.encode('rot13')
##    print deci.lower()
    s.send(deci+'\n')

def invi(deci):
    deci = deci.replace('.','1')
    deci = deci.replace('-','0')
    deci = deci.replace('0','.')
    deci = deci.replace('1','-')
    return deci
    
def morseInv():
    new = ''
    while not 'Decrypt' in new:
        new = s.recv(1024)
    r2 = re.compile("Decrypt (.*?)\n")
    deci = r2.findall(new)[0]
    deci = invi(deci)
    deci = decrypt(deci)
    s.send(deci+'\n')

def multiC(s):
    return ''.join([chr(((ord(i)-ord('A'))*9)%26 + ord('A')) for i in s])

def betteS(s,n):
    new = ['a']*len(s)
    for i in range(len(s)):
            new[i] = s[i*n%len(s)]
    return ''.join(new)

def morseMul():
    new = ''
    while not 'Decrypt' in new:
        new = s.recv(1024)
    print new
    r2 = re.compile("Decrypt (.*?)\n")
    deci = decrypt(r2.findall(new)[0])
    print deci
    if len(deci) == 5:
        ni = 2
    elif len(deci) == 8:
        ni = 3
    else:
        ni = len(deci)%5
        
    deci = betteS(deci,ni)
    s.send(deci+'\n')

            

def splitAndMerge(s,n):
    if len(s)%n != 0 :
        s += ' '
    tmp = [s[i:i+n] for i in range(0,len(s),n)]
    print tmp
    
    print tmp
    bb = zip(*tmp)
    aa = []
    for i in bb:
        aa += i

    return ''.join(aa)




def morseTr():
    new = ''
    while not 'Decrypt' in new:
        new = s.recv(1024)
    r2 = re.compile("Decrypt (.*?)\n")
    deci = decrypt(r2.findall(new)[0])
    deci = bruteDecrypt(deci)
##    print deci
    s.send(deci+'\n')

def level4():
    new = ''
    while not 'Decrypt' in new:
        new = s.recv(1024)
    r2 = re.compile("Decrypt (.*?)\n")
    deci = decrypt(r2.findall(new)[0])
    deci = bruteDecrypt(deci)
    deci = deci.encode('rot13')
##    print deci
    s.send(deci+'\n')


def level5():
    new = ''
    while not 'Decrypt' in new:
        new = s.recv(1024)
    r2 = re.compile("Decrypt (.*?)\n")
    deci = r2.findall(new)[0]
    deci = decrypt(invi(deci))
    deci = bruteDecrypt(deci)
    deci = deci.encode('rot13')
##    print deci
    s.send(deci+'\n')


def level6():
    new = ''
    while not 'Decrypt' in new:
        new = s.recv(1024)
    r2 = re.compile("Decrypt (.*?)\n")
    deci = r2.findall(new)[0]
    deci = decrypt(deci)
    deci = weirdo(deci)
##    print deci
    s.send(deci+'\n')

def level7():
    new = ''
    while not 'Decrypt' in new:
        new = s.recv(1024)
    r2 = re.compile("Decrypt (.*?)\n")
    deci = r2.findall(new)[0]
    deci = decrypt(invi(deci))
    deci = bruteDecrypt(deci)
    deci = weirdo2(deci)
    print deci
    s.send(deci+'\n')
    
def bruteDecrypt(s):
    if len(s) == 5:
        return betteS(s,2)
    elif len(s) == 6:
        return ''.join(fence(s,2))
    elif len(s) == 7:
        return se7en(s)
    elif len(s) == 8:
        return betteS(s,3)
    elif len(s) == 9:
        return nin9(s)
    elif len(s) == 10:
        return t3n(s)
    elif len(s) == 11:
        return eleven(s)
    elif len(s) == 12:
        return eleven(s)+s[11]
    elif len(s) == 13:
        return thirteen(s)
    elif len(s) == 14:
        return betteS(s,5)
    elif len(s) == 15:
        return betteS(s[:-1],5) + s[14]
    else:
        print 'no: %s'%s
            
      



print s.recv(1024)
s.send('la\n')


print "================Level 0=============="
for i in range(50):
    morse()

tmp= s.recv(2048)
s.send('hello\n')

print "================Level 1=============="
for i in range(50):
    morse13()

print "================Level 2=============="
tmp=s.recv(2048)
s.send('hello\n')

for i in range(50):
    morseInv()
print "================Level 3=============="
tmp=s.recv(2048)
s.send('abcdefghijklmno\n')

for i in range(50):
    morseTr()

print "================Level 4=============="
tmp= s.recv(2048)
s.send('hello\n')

for i in range(50):
    level4()

print "================Level 5=============="
tmp = s.recv(2048)
s.send('hello\n')

for i in range(50):
    level5()
    
print "================Level 6=============="
tmp = s.recv(2048)
s.send('hello\n')

for i in range(50):
    level6()

print "================Level 7=============="
tmp = s.recv(2048)
s.send('hello\n')

for i in range(50):
    level7()

tmp = s.recv(2048)
s.send('abcdefghijklmno\n')
print s.recv(1024)


