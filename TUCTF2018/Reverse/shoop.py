import string

s = string.ascii_lowercase[0:0x15]

src =''

a = 0

src = s[::-1]

print s
print src
src = list(src)

s = list(s)
for j in range(0x15):
    src[j] = chr(ord(src[j]) - 5)

print src
s = src
src = ['']*0x15
for k in range(0x15):
    src[k] = s[(k+10)%0x15]


    
def decrypt(s):
    new = ['']*0x15
    for k in range(0x15):
        new[k] = s[(k-10)%0x15]
    print new
    new2 = ['']*0x15
    for i in range(0x15):
        new2[i] = chr(ord(new[i])+5)
    return ''.join(new2[::-1])
        
