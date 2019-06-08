import z3
from utils import socki
from mt19937predictor import MT19937Predictor



def getString(tar):
    v1 = z3.BitVec('v1',32)
    v2 = z3.BitVec('v2',32)
    v3 = z3.BitVec('v3',32)

    s = z3.Solver()
    lol = "BCDGPTVZ"

    tar0=lol.index(tar[0])
    tar1=lol.index(tar[1])
    tar2=lol.index(tar[2])
    tar3=lol.index(tar[3])
    tar4=lol.index(tar[4])
    tar5=lol.index(tar[5])
    tar6=lol.index(tar[6])
    tar7=lol.index(tar[7])
    tar8=lol.index(tar[8])
    tar9=lol.index(tar[9])
    tar10=lol.index(tar[10])
    tar11=lol.index(tar[11])
    tar12=lol.index(tar[12])
    tar13=lol.index(tar[13])
    tar14=lol.index(tar[14])
    tar15=lol.index(tar[15])
    tar16=lol.index(tar[16])
    tar17=lol.index(tar[17])
    tar18=lol.index(tar[18])
    tar19=lol.index(tar[19])
    tar20=lol.index(tar[20])
    tar21=lol.index(tar[21])
    tar22=lol.index(tar[22])
    tar23=lol.index(tar[23])
    tar24=lol.index(tar[24])
    tar25=lol.index(tar[25])
    tar26=lol.index(tar[26])
    tar27=lol.index(tar[27])
    tar28=lol.index(tar[28])
    tar29=lol.index(tar[29])
    tar30=lol.index(tar[30])
    tar31=lol.index(tar[31])
        
    s.add(v2 >> 0x1F & 0x1 | v3 >> 0x0 & 0x3== tar0 )
    s.add(v1 >> 0x09 & 0x7== tar1 )
    s.add(v3 >> 0x05 & 0x7== tar2 )
    s.add(v3 >> 0x08 & 0x7== tar3 )
    s.add(v1 >> 0x15 & 0x7== tar4 )
    s.add(v1 >> 0x06 & 0x7== tar5 )
    s.add(v3 >> 0x1D & 0x7== tar6 )
    s.add(v1 >> 0x1B & 0x7== tar7 )
    s.add(v2 >> 0x04 & 0x7== tar8 )
    s.add(v2 >> 0x0D & 0x7== tar9 )
    s.add(v2 >> 0x0A & 0x7== tar10 )
    s.add(v3 >> 0x1A & 0x7== tar11 )
    s.add(v2 >> 0x16 & 0x7== tar12 )
    s.add(v3 >> 0x17 & 0x7== tar13 )
    s.add(v2 >> 0x1C & 0x7== tar14 )
    s.add(v3 >> 0x14 & 0x7== tar15 )
    s.add(v2 >> 0x01 & 0x7== tar16 )
    s.add(v3 >> 0x11 & 0x7== tar17 )
    s.add(v1 >> 0x00 & 0x7== tar18 )
    s.add(v2 >> 0x13 & 0x7== tar19 )
    s.add(v1 >> 0x18 & 0x7== tar20 )
    s.add(v3 >> 0x0B & 0x7== tar21 )
    s.add(v2 >> 0x19 & 0x7== tar22 )
    s.add(v2 >> 0x10 & 0x7== tar23 )
    s.add(v1 >> 0x03 & 0x7== tar24 )
    s.add(v1 >> 0x12 & 0x7== tar25 )
    s.add(v1 >> 0x0F & 0x7== tar26 )
    s.add(v3 >> 0x02 & 0x7== tar27 )
    s.add(v1 >> 0x0C & 0x7== tar28 )
    s.add(v2 >> 0x07 & 0x7== tar29 )
    s.add(v3 >> 0x0E & 0x7== tar30 )
    s.add(v1 >> 0x1E & 0x3 | v2 >> 0x00 & 0x1== tar31 )
##    s.add(v1 < 1000)
##    s.add(v2 < 1000)
##    s.add(v3 < 1000)

    #print s
    s.check()
    return [s.model()[v1].as_long(),s.model()[v2].as_long(),s.model()[v3].as_long()]



def getValues():
    s = socki('misc.hsctf.com 9988')
    acts = s.recv(10000)
    act = acts.split('\n')
    act2 = act[8:-2]
    assert(len(act2) == 216)
    tab = []
    for i in act2:
        tab.extend(getString(i))
    return tab

def testSeed(s):
    seed = s[624:]
    predic = MT19937Predictor()
    for i in seed:
        predic.setrandbits(i,32)
    if predic.getrandbits(32) == s[624]:
        print 'noice'
    else:
        print 'nope'
    
    
