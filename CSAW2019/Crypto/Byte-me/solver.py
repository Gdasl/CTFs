from utils import socki
import time
import string

alpha = '{}_.,'+string.digits + string.ascii_letters
alpha = alpha + alpha + string.printable

s = socki('crypto.chal.csaw.io 8080')

flag = s.recv(1024).split('\r\n')[0]

def send(m):
    s.send(m+'\n')
    time.sleep(0.5)
    return s.recv(1024).split('\r\n')[1]



firstLetter = send('a'*15)[0:32]

def blocki(s,i):
    return [s[j:j+i] for j in range(0,len(s),i)]



def most_frequent(List): 
    return max(set(List), key = List.count)


def findRandLen():
    init = len(blocki(flag,32))
    for i in range(1,16):
        if len(blocki(send('g'*i),32)) > init:
            return i-1





def test():
    i = 0
    init = blocki(send('a'*(64)),32)
    
    tmp = most_frequent(init)
    while init.count(tmp) != 4:
        i+=1
        init = blocki(send('a'*(64 + i)),32)
    return i + 64
        

def findLetter(i,pre=''):
    target = blocki(send('a'*(i-1 - len(pre))),32)[-4]

    for c in alpha:
        tmp = blocki(send('a'*(i-1 - len(pre)) + pre + c),32)[-4]
        if tmp == target:
            return c
    return target



def findLetter(i,pre='',block = 4):
    target = blocki(send('a'*(i-1 - len(pre))),32)[block]

    for c in alpha:
        tmp = blocki(send('a'*(i-1 - len(pre)) + pre + c),32)[block]
        if tmp == target:
            return c
    return target



pre = ""
ori = test()
while True:
    tmp = findLetter(ori,pre)
    pre += tmp
    print pre

