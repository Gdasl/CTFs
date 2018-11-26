#!/usr/bin/env python2
from cryptoHelper import *

def xor(msg, key):
    o = ''
    for i in range(len(msg)):
        o += chr(ord(msg[i]) ^ ord(key[i % len(key)]))
    return o

def enci():
    with open('message', 'r') as f:
        msg = ''.join(f.readlines()).rstrip('\n')

    with open('key', 'r') as k:
        key = ''.join(k.readlines()).rstrip('\n')

    assert key.isalnum() and (len(key) == 9)
    assert 'TUCTF' in msg

    with open('encrypted', 'w') as fo:
        fo.write(xor(msg, key))

mess = open('encrypted','rb').read()


six = mess
def go():
    actual = breakblock(six,9)
    jiji = inverse(actual)
    stri = ''
    loss = []
    tempi = []
    for j in jiji:
        flag = 1
        for i in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if checkprintableXtreme(xorarr(j,i)):
                    print xorarr(j,i)
                    tempi.append(xorarr(j,i))
                    print "key: " + i
                    stri+=i
                    flag = 0
        if flag:
             loss.append(j)

    if len(stri) != len(jiji):
        print "Warning, string not complete"
    return stri, tempi,loss
