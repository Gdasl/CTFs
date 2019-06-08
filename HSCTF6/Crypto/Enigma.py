from enigma.rotors.rotor import Rotor
from enigma.machine import EnigmaMachine
import string
import itertools

"""
Implies you install pyenigma from pypy
"""

alphabet = string.ascii_uppercase
ct = 'JGYJZ NOXZX QZRUQ KNTDN UJWIA ISVIN PFKIR VWKWC UXEBH RFHDI NMOGQ BPRHW CXGAC ARBUN IHOWH QDDGL BBZYH HEJMV RBLJH CLHYP FSAAA KNRPX IKSNX QASGI XBMNP FLAFA KFEGV YWYUN JGBHH QDLZP UJWMO CCEUL YFIHR GTCOZ GEQML VFUAV URXUU BBGCI YZJQQ ROQFU SJDVR JILAJ XYCBC IGATK LQMAP UDPCG ONWFV MHBEC CLBLP JHZJN HMDNY YATIL FQSND AOCAM MGVRZ FEVKL CEDMG AIWXG QPCBI VTVZU HQGFD ZJICI EIWLP IFKAB LNVZI XRZTR SLGCA SZPFF HGBUK JAXNN JHUSV UFPIM ZZLAW SYOHB TOLRF KWANX FNEFD XXLNR LLGYS VTGXP NJQMC WAKRP JKWDP WVTNP WRYEJ RSODI QDYOQ DJDBI SLAVB UPDDR ATHYG ANJQR XPGFM FAMJR ZSJHC SYWQQ VBIHX XCQFW XZBUH ZRXWV TPESM EGVVY PBJSS'

def test(li,deb=False):
    rs = ' '.join([str(i) for i in li])
    #print rs
    try:
        machine = EnigmaMachine.from_key_sheet(
               rotors='III II IV',
               reflector='B',
               ring_settings=rs,
               plugboard_settings='DE AH CO GZ LQ NY PS TW IJ KM')

        machine.set_display('EFM')
        c = machine.process_text('XTSYN WAEUG EZALY NRQIM', replace_char=None)
        if deb:
            print c
        if 'HELLO' in c:
            print i,j,k
    except Exception as e:
        pass


def testRot3(var1,var2):
    rs = 'A A '+var1
    machine = EnigmaMachine.from_key_sheet(
               rotors='III II IV',
               reflector='B',
               ring_settings=rs,
               plugboard_settings='CT EW JL QX')
    machine.set_display('SE'+var2)
    c = machine.process_text('JGYJZ NOXZX QZRUQ KNTDN UJWIA', replace_char=None)
    return c

def testRot2(var1,var2):
    rs = 'A '+var1 + ' A'
    machine = EnigmaMachine.from_key_sheet(
               rotors='III II IV',
               reflector='B',
               ring_settings=rs,
               plugboard_settings='CT EW JL QX')
    machine.set_display('S'+var2+'P')
    c = machine.process_text('JGYJZ NOXZX QZRUQ KNTDN UJWIA', replace_char=None)
    return c

def testRot1(var1,var2):
    rs = var1 + ' A A'
    machine = EnigmaMachine.from_key_sheet(
               rotors='III II IV',
               reflector='B',
               ring_settings=rs,
               plugboard_settings='CT EW JL QX')
    machine.set_display(var2+'EP')
    c = machine.process_text('JGYJZ NOXZX QZRUQ KNTDN UJWIA', replace_char=None)
    return c

def testAllVars(r1_0,r1_1,r2_0,r2_1,r3_0,r3_1):
    rs = ' '.join([r1_0,r2_0,r3_0])
    machine = EnigmaMachine.from_key_sheet(
               rotors='III II IV',
               reflector='B',
               ring_settings=rs,
               plugboard_settings='CT EW JL QX')
    machine.set_display(''.join([r1_1,r2_1,r3_1]))
    c = machine.process_text('JGYJZ NOXZX QZRUQ KNTDN UJWIA', replace_char=None)
    return c
                        

posRot2 = [('B', 'F'), ('C', 'G'), ('D', 'H'), ('E', 'I'), ('F', 'J'), ('G', 'K'), ('H', 'L'), ('I', 'M'), ('J', 'N'), ('K', 'O'), ('L', 'P'), ('M', 'Q'), ('N', 'R'), ('O', 'S'), ('P', 'T'), ('Q', 'U'), ('R', 'V'), ('S', 'W'), ('T', 'X'), ('U', 'Y'), ('V', 'Z'), ('W', 'A'), ('X', 'B'), ('Y', 'C'), ('Z', 'D')]

    
def getDelta(pb):
    li = []
    pb = pb.replace(' ','')
    for i in string.ascii_uppercase:
        if i not in pb:
            li.append(i)

    return li

pb1 = 'CT EW JL QX'
pb2 = 'EK BC DQ LP MN RT SU XZ AG'
li2 = [''.join(i) for i in itertools.combinations(getDelta('CT EW JL QX'),2)]
li3 = [''.join(i) for i in itertools.combinations(getDelta(pb2),2)]

pos2 = 'ECG'

def testVarsSb(r1_0,r1_1,r2_0,r2_1,r3_0,r3_1,pb,cip=None):
    if cip is None:
        cip = 'JGYJZ NOXZX QZRUQ KNTDN UJWIA'
    rs = ' '.join([r1_0,r2_0,r3_0])
    machine = EnigmaMachine.from_key_sheet(
               rotors='III II IV',
               reflector='B',
               ring_settings=rs,
               plugboard_settings=pb)
    machine.set_display(''.join([r1_1,r2_1,r3_1]))
    c = machine.process_text(cip, replace_char=None)
    return c

def getOffset(v1,v2):
    return (string.ascii_uppercase.index(v2)-string.ascii_uppercase.index(v1))%26


p2 = 4
p1 = getOffset('A','S')
p3 = getOffset('A','P')


def generateList(offset):
    tmp = []
    for i in alphabet:
        tmp.append((i,alphabet[(alphabet.index(i)+offset)%26]))
    return tmp

possible1 = generateList(p1)
possible2 = generateList(p2)
possible3 = generateList(p3)

## pos3 is GM

print testVarsSb('Z','D','A','C','G','M',pb2+' VF',ct)
