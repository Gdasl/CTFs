def fence(lst, numrails):
    fence = [[None] * len(lst) for n in range(numrails)]
    rails = range(numrails - 1) + range(numrails - 1, 0, -1)
    for n, x in enumerate(lst):
        fence[rails[n % len(rails)]][n] = x

    if 0: # debug
        for rail in fence:
            print ''.join('.' if c is None else str(c) for c in rail)

    return [c for rail in fence for c in rail if c is not None]

def encodeF(text, n):
    return ''.join(fence(text, n))

def decode(text, n):
    rng = range(len(text))
    pos = fence(rng, n)
    return ''.join(text[pos.index(n)] for n in rng)


def se7en(s):
    new = ['']*7
    new[0] = s[0]
    new[1] = s[3]
    new[2] = s[5]
    new[3] = s[1]
    new[4] = s[4]
    new[5] = s[6]
    new[6] = s[2]
    return ''.join(new)


def nin9(s):
    new = ['']*9
    new[0] = s[0]
    new[1] = s[3]
    new[2] = s[6]
    new[3] = s[1]
    new[4] = s[4]
    new[5] = s[7]
    new[6] = s[2]
    new[7] = s[5]
    new[8] = s[8]
    return ''.join(new)

def t3n(s):
    new = ['']*10
    new[0] = s[0]
    new[1] = s[4]
    new[2] = s[7]
    new[3] = s[1]
    new[4] = s[5]
    new[5] = s[8]
    new[6] = s[2]
    new[7] = s[6]
    new[8] = s[9]
    new[9] = s[3]
    return ''.join(new)
    
def eleven(s):
    new = ['']*11
    new[0] = s[0]
    new[1] = s[4]
    new[2] = s[8]
    new[3] = s[1]
    new[4] = s[5]
    new[5] = s[9]
    new[6] = s[2]
    new[7] = s[6]
    new[8] = s[10]
    new[9] = s[3]
    new[10] = s[7]
    return ''.join(new)

def thirteen(s):
    new = ['']*13
    new[0] = s[0]
    new[1] = s[5]
    new[2] = s[9]
    new[3] = s[1]
    new[4] = s[6]
    new[5] = s[10]
    new[6] = s[2]
    new[7] = s[7]
    new[8] = s[11]
    new[9] = s[3]
    new[10] = s[8]
    new[11] = s[12]
    new[12] = s[4]
    return ''.join(new)



def weirdo(s):
    new = ''
    tr = [7,6,-2,7,-5,7,6,-2,7,-5,7,6,-2,7,-5]
    if len(s) > len(tr):
        print 'error'
    for i in range(len(s)):
        new+= chr((ord(s[i]) - ord('A') + tr[i]) % 26 + ord('A'))

    return new


def weirdo2(s):
    new = ''
    tr = [-7,0,5,-4,-5,6,13,-7,0,5,-4,-5,6,13,19]

    for i in range(len(s)):
        new+= chr((ord(s[i]) - ord('A') + tr[i]) % 26 + ord('A'))

    return new
        
