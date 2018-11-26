import base64

stri = 'MTAxMTAxMDEwMTExMDEwMTAwMTAxMDEwMTExMTAxMDEwMTEwMTAxMDAxMDExMDEwMTAwMTExMTAxMDEwMTExMDAxMDEwMTAxMTEwMDEwMTAxMDEwMDExMDEwMTAwMDAwMDAxMDEwMTAwMTExMTAxMDEwMDAwMDAxMDEwMTAwMDAwMDEwMTAxMDEwMDExMDEwMTAwMDAwMDAxMDEwMTAwMTExMTAxMDEwMDAwMDAxMDEwMTAwMDAwMDEwMTAxMDEwMDExMDEwMTAwMDAwMDAxMDEwMTAwMTExMTAxMDEwMTExMDAxMDEwMTAxMTEwMDEwMTAxMDEwMDExMDEwMTA='

bdec = base64.decodestring(stri)

def splitti(stri,n):
    return [stri[i:i+n] for i in range(0,len(stri),n)]


def convertToBase(arr,base):
    tmp = ''.join([str(int(i,2)) for i in arr])
    return int(tmp,base)


def convertToBaseStr(arr):
    tmp = ''.join([chr(int(i,2)) for i in arr])
    return tmp


import string
