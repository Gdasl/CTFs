f = open('binobs.txt','rb').read()

import sys
import os
import codecs
import StringIO
if len(sys.argv) == 2:
    stream = codecs.open(sys.argv[1], encoding='utf-8')
else:
    sys.stdin = codecs.getreader('utf-8')(sys.stdin)
    stream = sys.stdin
s = [-1,0,0,0,0,0,0]
while 1:
    buf = stream.read(4)
    if buf[0] == unichr(0xff0c):
        extralen = len(stream.read())+len(buf)
        for i in s[0:7-extralen]:
            sys.stdout.write(chr(i))
        break
    if s[0] != -1:
        for i in s:
            sys.stdout.write(chr(i))
    buf = map(lambda x:ord(x)-0x4e00,buf)
    s[0] = buf[0]>>6
    s[1] = ((buf[0] % 64) << 2) + (buf[1]>>12)
    s[2] = (buf[1] >> 4) % 256
    s[3] = ((buf[1] % 16) << 4) + (buf[2]>>10)
    s[4] = (buf[2] >> 2) % 256
    s[5] = ((buf[2] % 4 ) << 6) + (buf[3]>>8)
    s[6] = (buf[3]) % 256
