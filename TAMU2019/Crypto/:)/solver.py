import base64

def xor(a,b):
  return ''.join([chr(ord(a[i])^ord(b[i%len(b)])) for i in range(len(a))])
  
s = 'XUBdTFdScw5XCVRGTglJXEpMSFpOQE5AVVxJBRpLT10aYBpIVwlbCVZATl1WTBpaTkBOQFVcSQdH'

print xor(base64.decodestring(s),':)')
