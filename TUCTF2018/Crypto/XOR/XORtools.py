"""
Set 1
"""

import binascii
import base64
import operator

import unittest

from Crypto.Cipher import AES

## Challenge 1:
# Convert hex to base64

def hex_to_base64(hex_str):
    # convert to raw bytes
    bin_data = hex_str.decode('hex')

    # encode in b64
    return base64.b64encode(bin_data)


## Challenge 2:
# Fixed XOR

def fixed_xor(hex_str1, hex_str2):
    assert len(hex_str1) == len(hex_str2)
    
    bin1 = hex_str1.decode('hex')
    bin2 = hex_str2.decode('hex')

    xor_result = "".join([chr(ord(a) ^ ord(b)) for (a,b) in zip(bin1, bin2)])

    return xor_result.encode('hex')
    
    
## Challenge 3
# Single byte xor cipher

# Returns list of likely mappings
# ciphertext is ascii
def key_search(ciphertext):

    count_dict = {}
    percent_dict = {}

    import re
    for k in range(256):
        # apply the key
        plaintext = "".join(chr(k ^ ord(c)) for c in ciphertext)

        plaintext = plaintext.lower()

        # get histogram
        count = len(re.findall('[etaoin shrdlu]', plaintext))
        percentage = float(count)/len(ciphertext)
        if percentage > 0.6:
            print "Potential match for k = %d" % k
            percent_dict[percentage] = k

        count_dict[count] = k

    keys_by_raw_count = []
    for k in sorted(count_dict.keys(), reverse=True):
        keys_by_raw_count.append(count_dict[k])

    keys_by_percentage = []
    for k in sorted(percent_dict.keys(), reverse=True):
        keys_by_percentage.append(percent_dict[k])

    #print "Keys by raw count:", keys_by_raw_count
    #print "Keys by percentage:", percent_dict

    if len(keys_by_percentage) > 0:
        return keys_by_percentage
    else:
        return keys_by_raw_count

def single_byte_xor(hex_str):
    # guess the key based on freq analysis

    ciphertext = [int("".join((a,b)),16) for (a,b) in zip(hex_str[0::2],
                                                        hex_str[1::2])]

    ciphertext = "".join(chr(c) for c in ciphertext)

    keys = key_search(ciphertext)
    k = keys[0]

    #print "Trying key %d" % k

    # try to decode
    return "".join([chr(k ^ ord(c)) for c in ciphertext])



## Challenge 4
# Detect Single Character XOR

def detect_single_char_xor(filename):
    f = open(filename, 'r')

    msgs = f.readlines()
    for msg in msgs:
        p = single_byte_xor(msg)

        # simple check
        if all(ord(c) < 128 for c in p):
            print p

        # better check?
#        try:
#            p.decode('ascii')
#            print p
#        except UnicodeDecodeError:
#            #print "Not a valid printable msg.  Skipping."

    f.close()



## Challenge 5
# Implement repeating key XOR cipher

def repeat_key_XOR(key, plaintext):
    ciphertext = range(len(plaintext))
    k_index = 0

    for i in range(len(plaintext)):
        ciphertext[i] = ord(key[k_index]) ^ ord(plaintext[i])
        k_index = (k_index + 1) % len(key)

    return "".join([chr(c).encode('hex') for c in ciphertext])


## Challenge 6
# Breaking repeating key XOR

def hamming_dist(str1, str2):
    """
    :param str1: ascii string
    :param str2: ascii string
    :return: number of differing bits
    """
    if len(str1) != len(str2):
        raise "Incompatible length for Hamming distance"

    dist = 0

    for i in range(len(str1)):
        c = ord(str1[i]) ^ ord(str2[i])

        dist += bin(c).count("1")

    return dist

def do_xor(key, text):
    k_index = 0
    ret = range(len(text))
    for i in range(len(text)):
        ret[i] = ord(key[k_index]) ^ ord(text[i])
        k_index = (k_index + 1) % len(key)

    return "".join([chr(c) for c in ret])

def break_repeat_key_XOR(ciphertext):
    """
    :param ciphertext: ascii
    :return:
    """

    print "Length of ciphertext is %d" % len(ciphertext)

    # try to guess the key size
    normalized_hamming_dist = {}
    for keysize in range(9,10):

        hd = 0
        n = len(ciphertext)/keysize
        for i in range(1, n):
            hd += hamming_dist(ciphertext[0:keysize],
                               ciphertext[keysize*i: keysize*(i+1)])
        hd_normalized = (float(hd)/(n-1))/keysize

        normalized_hamming_dist[hd_normalized] = keysize

    for k in sorted(normalized_hamming_dist.keys()):
        print normalized_hamming_dist[k], k

    num_key_sizes = 1
    for k in sorted(normalized_hamming_dist.keys()):

        if num_key_sizes < 1:
            break
        num_key_sizes -= 1

        keysize = normalized_hamming_dist[k]

        print "Trying keysize of %d" % keysize
        # break ciphertext into blocks where each block contains
        # the ith character of each keysize block

        block_list = []
        for i in range(keysize):
            block = []
            for j in range(i, len(ciphertext), keysize):
                block.append(ciphertext[j])
            block_list.append("".join(block))

        # now try to break single char xor
        key = []
        for i in range(len(block_list)):
            k = key_search(block_list[i])[0]
            #print "Guessing key at %d is %s" % (i,chr(k))
            key.append(k)

        print "Guessing key is ", key

        print "Decoded message: "
        key = "".join([chr(k) for k in key])
        plaintext = do_xor(key, ciphertext)

        print "".join(plaintext)

        print ""



## Challenge 7
# AES ECB mode

def aes_ecb_128(key, ciphertext):
    c = AES.new(key, AES.MODE_ECB)
    return c.decrypt(ciphertext)


## Challenge 8
# Detect ECB mode

# assumes input in hex
def detect_ecb(ciphertext, block_size=16):
    d = {}
    for i in range(0, len(ciphertext), block_size*2):
        d[ciphertext[i:i+block_size*2]] = d.get(ciphertext[i:i+block_size*2], 0) + 1

    repeats = 0
    for k in d:
        if d[k] > 1:
            repeats += 1

    return repeats > 0


def main():


    print "Testing Challenge 1:"
    print "---------------------"
    input_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print "The following should be equal: "
    print hex_to_base64(input_hex)
    print 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'


    print "\n\n"

    print "Testing Challenge 2:"
    print "---------------------"
    input_hex1 = '1c0111001f010100061a024b53535009181c'
    input_hex2 = '686974207468652062756c6c277320657965'
    print "The following should be equal: "
    print fixed_xor(input_hex1, input_hex2)
    print '746865206b696420646f6e277420706c6179'

    print "\n\n"

    print "Testing Challenge 3:"
    print "---------------------"
    input_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    print single_byte_xor(input_hex)

    print "\n\n"

##    print "Testing Challenge 4:"
##    print "---------------------"
##    fname = '4.txt'
##    detect_single_char_xor(fname)
##
##    print "\n\n"
##
##
##    print "Testing Challenge 5:"
##    print "---------------------"
##    input_str = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
##
##    output = repeat_key_XOR("ICE", input_str)
##    print input_str
##    print output
##
##    print "\n\n"


    print "Testing Challenge 6:"
    print "---------------------"

    #print hamming_dist("this is a test", "wokka wokka!!!")
    fname = '6.txt'
    ciphertext = open('encrypted','rb').read()

    break_repeat_key_XOR(ciphertext)

    print "\n\n"

##
##    print "Testing Challenge 7:"
##    print "---------------------"
##    fname = '7.txt'
##
##    f = open(fname, 'r')
##
##    # convert base64
##    ciphertext = base64.b64decode(f.read())
##    f.close()
##	
##
##    k = b'YELLOW SUBMARINE'
##
##    print aes_ecb_128(k, ciphertext)
##
##    print "\n\n"
##
##
##    print "Testing Challenge 8:"
##    print "---------------------"
##    fname = '8.txt'
##
##    f = open(fname, 'r')
##    lines = f.readlines()
##    f.close()
##
##    print "Read %d total lines" % len(lines)
##
##    for i in range(len(lines)):
##        r = detect_ecb(lines[i])
##        if r > 0:
##            print lines[i]
##            print "line %d, %d repeated blocks" % (i, r)
##
##    print "\n\n"

if __name__=='__main__':
    main()
