from pwn import *
import string
noice = string.ascii_letters+string.digits +'{}_'

print "succesful import"

def split(s,l):
    return [s[i:i+l*2] for i in range(0,len(s)-l*2,l*2)]



first =  '    My agent identifying code ' ##gives first letter
##blocki = split(go(first),16)[7] ##block containing first letter of flag##

first_test = '    My agent identifying code is: ' ##needs char added

def runit(fi,ft):
    for j in range(32):
        r = remote('2018shell2.picoctf.com', 34490)
        print r.recvuntil('ort: ')
        r.sendline(fi[j:])
        base = r.recv()
        print base
        r.close()
        for i in noice:
            r = remote('2018shell2.picoctf.com', 34490)
            r.recvuntil('ort: ')
            r.sendline(ft[j:]+i)
            ans = r.recv()
            r.close()
            print ans
            if split(ans,16)[5] == split(base,16)[7]:
                ft = ft+i 
                print i
                break


def testq(s):
    r = remote('2018shell2.picoctf.com', 34490)
    r.recvuntil('ort: ')
    r.sendline(s)
    return r.recv()
