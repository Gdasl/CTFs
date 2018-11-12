import base64
from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode
from fontTools.ttLib.tables import _c_m_a_p
from itertools import chain
import webbrowser
import win32clipboard
import re
import requests

atWork = False

import win32api, win32con
import win32com.client
import time
#import SendKeys
import os
from ctypes import *


def getSourceAndCopy():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('^u')
    shell.SendKeys('^a')
    shell.SendKeys('^c')
    shell.SendKeys('^c')
    shell.SendKeys('^c')

def getSource():
    if atWork:
        webbrowser.open(url)
        time.sleep(0.5)
        getSourceAndCopy()
        time.sleep(0.1)
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    else:
        data = requests.get(url).text
    return data


    
url = 'https://hidden-island-93990.squarectf.com/ea6c95c6d0ff24545cad'


def dumpTofFile(d, fn = 'new'):
    f = open(fn,'wb')
    f.write(base64.decodestring(d))
    f.close()

def printChars(f):
    ttf = TTFont(f)
    chars = chain.from_iterable([y + (Unicode[y[0]],) for y in x.cmap.items()] for x in ttf["cmap"].tables)
    a = list(chars)
    return a


mapping = {'0':'glyph00005',
           '1':'glyph00012',
           '2':'glyph00006',
           '3':'glyph00011',
           '4':'glyph00007',
           '5':'glyph00010',
           '6':'glyph00013',
           '7':'glyph00002',
           '8':'glyph00008',
           '9':'glyph00001',
           '*':'glyph00009',
           '-':'glyph00014',
           '(':'glyph00015',
           ')':'glyph00004',
           '+':'glyph00003' 
    }
orig = printChars('new.ttf')


def diciFromLi(li):
    return [{i[1]:chr(i[0])} for i in li]

def retCoordsOrig():
    ttf = TTFont('new.ttf')
    dici = {}
    for i in mapping:
        dici[i] = str(ttf['glyf'][mapping[i]].__dict__['coordinates'])
    return dici

def retCoordsMap(f):
    dici = {}
    mapi = printChars(f)
    ttf = TTFont(f)
    for i in mapi:
        dici[str(ttf['glyf'][i[1]].__dict__['coordinates'])]= chr(i[0])
    return dici
        
diciOrig = retCoordsOrig()



def findCharMapping(d1,d2):
    dici = {}
    for i in d1:
        dici[d2[d1[i]]] = i
    return dici
    


def dumpitStraight():
    t = time.time()
    aloha = getSource()
    r = re.compile("charset=utf-8;base64,(.*?)'")
    r2 = re.compile("<h1>Captcha</h1><p>(.*?)</p><html><body>")
    r3 =re.compile('name="token" value="(.*?)"><input')
    captcha = r2.findall(aloha)[0]
    token = r3.findall(aloha)[0]
    print token
    dumpTofFile(r.findall(aloha)[0], fn = 'test.ttf')
    diciNew = retCoordsMap('test.ttf')
    diciFin = findCharMapping(diciOrig, diciNew)

    for k,v in diciFin.iteritems():
        captcha = captcha.replace(k, v)
    print "Captcha: %s"%captcha

    tmp = eval(captcha)
    print "Total time: %d" %(time.time() - t)
    data={'token': int(token), 'answer': str(tmp)}
    print requests.post(url, data=data).text
    return str(tmp)
    

