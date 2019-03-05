from Arithmetic import *
n = 2531257
e = 43

q = 509
p = 4972

m = '906851 991083 1780304 2380434 438490 356019 921472 822283 817856 556932 2102538 2501908 2211404 991083 1562919 38268'

phi = (p-1)*(q-1)
d = modInv(e,phi)

arr = []
for i in m.split(' '):
  arr.append(pow(int(i),d,n))

arr2 = []
for i in arr:
	if i < 256:
		arr2.append(chr(i))
	else:
		if int(str(i)[:2]) < 256 and int(str(i)[:2]) > 32:
			arr2.extend([chr(int(str(i)[:2])),chr(int(str(i)[2:]))])
		else:
			arr2.extend([chr(int(str(i)[:3])),chr(int(str(i)[3:]))])
      
print ''.join(arr2)
