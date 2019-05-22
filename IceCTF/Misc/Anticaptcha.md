# Anticaptcha

> Wow, this is a big captcha. Who has enough time to solve this? Seems like a lot of effort to me!

## The setup
We are given a webpage with a bunch of captchas (around 600), where you have to find gcd, primality or other asinine stuff. 

## The solving
Looking back, submitting an empty form always returned ```6 questions wrong``` which should have tipped me off that there were only 6 special questions to be answered. However, I went the hard way and scripted an auto parser that splits the initial response when calling the website into it's parts, analyses each question and adds the answer to an array (I had all the scripts already). There were 6 sepcial questions about capitals and mountains which I hardcoded like a dumbass. Running the script then returned the flag. Easy as pie.


Script used:
```python
import requests
from fractions import gcd
from MillerRabin import *

ur = "https://e4lpq683c5y2jsd-anticaptcha.labs.icec.tf/"


aa = requests.get(ur)
qq = aa.text.split('<td>')
intro = qq[0]

qs = []
for i in range(1,len(qq),2):
    qs.append(str(qq[i]).replace('?', ' '))
    


#q types

cmdv = 'What is the greatest common'
line = 'word in the following line'
prime = 'a prime number'

jaws = 'directed the movie Jaws'
pln = 'planet is closest to the '
mt = 'hat is the tallest mountain on Earth'
sun = 'How many planets are between Earth and the Sun'
yr = 'What year is it'
grm = 'What is the capital of Germany'
sky = 'What color is the sky'
viol = 'How many strings does a violin have'
haw = 'What is the capital of Hawaii'

ansis = []
for i in qs:
    if cmdv in i:
        tmp = [int(s) for s in i[:-6].split() if s.isdigit()]
        try:
            assert(len(tmp) == 2)
        except Exception as e:
            print tmp
            print i[:-6]
        ansis.append(str(gcd(tmp[0],tmp[1])))
        
    elif line in i:
        tmp = i.split()
        num = int(tmp[3][0:len(tmp[3])-2])
        ansis.append(i.split(':')[1].split()[num-1].replace('.',''))
        
        
    elif prime in i:
        ansis.append(miller_rabin(int(i.split()[1])))
##        print i
        
    elif jaws in i:
        ansis.append('Steven Spielberg')
    elif pln in i:
        ansis.append('Mercury')
    elif mt in i:
        ansis.append('Everest')
    elif sun in i:
        ansis.append('2')
    elif yr in i:
        ansis.append('2018')
    elif grm in i:
        ansis.append('Berlin')
    elif sky in i:
        ansis.append('Blue')
    elif viol in i:
        ansis.append('4')
    elif haw in i:
        ansis.append('Honolulu')
    else:
        print i
        ans = raw_input()
        ansis.append(ans)
        
payload = []
for k in ansis:
    payload.append('answer='+str(k)+'&')
    


final = ''.join(payload) + 'submit=Submit+Answers'

f = open('tmp.txt','w')
f.write(final)
f.close()

#reqi = requests.post(ur,data = final)
