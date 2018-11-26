from Crypto.Cipher import AES
import binascii
import string

KEY='9aF738g9AkI112ii'
IV ='aaaaaaaaaaaaaaaa'

def encrypt(message, passphrase):
    aes = AES.new(passphrase, AES.MODE_CBC, IV)
    return aes.encrypt(message)


stri = "The message is protected by AES!"

printi = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!'
part = '436a808e200a54806b0e94fb9633db9d67f0'

def splitti(stri,n):
    return [stri[i:i+n] for i in range(0,len(stri),n)]


##for i in range(255):
##    for j in range(255):
##        KEY='9aF738g9AkI112'+chr(i)+chr(j)
##        print KEY
##        IV = '808e200a54806b0e'.encode('hex')
##        a = AES.new(KEY,AES.MODE_CBC,IV)
##        tmp = a.encrypt(stri[16:32])
##        if '94fb9633db9d67f0' in tmp.encode('hex'):
##            print 'found'
##        

arr =[]        
        
for i in printi:
    print i
    for j in printi:
        for k in printi:
            for h in printi:
                KEY='9aF738g9AkI112'+i+j
                IV = k+h + ('a'*14)
                a = AES.new(KEY,AES.MODE_CBC,IV)
                tmp = a.encrypt(stri).encode('hex')
                if tmp[0:2] == '9e' and tmp[16:18] == '80':
                    arr.append(tmp)
                
                
                
        
