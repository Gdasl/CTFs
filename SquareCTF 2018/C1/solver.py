import random
ttd = open('instructions.txt').read()

actual = ttd.split('.')

list_to_trans = [len(i) for i in actual]

def encode(s, verbose = False):
    a = []
    for i in range(len(s)):
        t = ord(s[i])
        for j in range(8):
            if ((t>>j) & 1):
                print j
                
                a.append(1+j+ (len(s) - 1 - i) * 8)

    print a
    b = []
    try:
        while len(a) > 0:
            t = int(random.random() * len(a)) | 0
            b.append(a[t])
            tmp = a[0:t]
            tmp2 = a[t+1:]
            
            a = tmp
            a.extend(tmp2)

    except Exception as e:
        print e

    print b
    r = ''
    for i in range(len(b)):
        t = b.pop()
        r += '-'*t + '.'
    if verbose:
        return r

def getJ(i):
    return i%8

def getChar(arr):
    arr.sort()
    ai_j = [getJ(i-1) for i in arr]
    print ai_j
    b = [0]*8
    for i in ai_j:
        b[i] = 1
    print b
    return chr(int(''.join(str(i) for i in b[::-1]),2))
    
def getLenght(arr):
    m = max(arr)
    return (m - m%8)/8 + 1


def spliti(arri):
    
    arri.sort()
    arri = arri[::-1]
    arri_j = [getJ(i) for i in arri]
    patient0 = arri_j[0]

    tmp = []
    tmp.append(arri[0])
    splitted = []
    for i in range(1,len(arri_j)):
        if arri_j[i] < patient0:
            tmp.append(arri[i])
        else:
            splitted.append(tmp)
            tmp = []
            tmp.append(arri_j[i])

        patient0 = arri_j[i]
    splitted.append(tmp)

    return splitted


def doAll(arr):
    return ''.join([getChar(i) for i in spliti(arr)])
    
 doAll(list_to_trans)
