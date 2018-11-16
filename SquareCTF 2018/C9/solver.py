buf = '1712009367807218646859018292134521568805686127287089876612468382748236461208592688982686121828975882178245515674851882'
chars = "1234567890abcdefg"
def xor(stri,key):
    return ''.join([chr(ord(stri[i]) ^ ord(key[i%len(key)])) for i in range(len(stri))])

key = '4L0ksa1t'

fir = "%"

def findNext(p,n):
    k = 0
    print "p:%d n:%d\n"%(p,n)
    for i in chars:
        tmp = xor(i,key[p%8])
        if buf[n:n+len(str(ord(tmp)))] == str(ord(tmp)):
            if len(str(ord(tmp))) > k:
                k = len(str(ord(tmp)))
                reti = i
    return reti,k
            
    
            

def solver(p,n,buf,fir):
    
    while n != len(buf):
        tmp,k = findNext(p,n)
        fir += tmp
        n += k
        print n
        print k
        p+=1
    return fir
        

sol = solver(1,2,buf,fir)

def encrypt_str(stri):
    key = '4L0ksa1t'
    n = 0
    buf = ""
    for i in range(len(stri)):
        buf += chr(ord(stri[i])^ord(key[i%8]))
    return buf
        
