# LZ78 Encoding
#
# Performs LZ78 encoding on the standard input and writes result to standard output
# using algorithm described in MacKay textbook.
# 
# Note:
#  - All input symbols are encoded using 7-bit ASCII.
#  - Pointer index is encoded using logarithmically increasing number of bits
#
# USAGE: python lz78-encode.py
#
# EXAMPLE:
#    $ echo "aaabbb" python lz78-encode.py 
#    01100001111000010011000101111000100001100010
#
# AUTHOR: Mark Reid <mark.reid@anu.edu.au>
# CREATED: 2013-10-21

import sys
import math
import logging
import bitarray

def encode(stream):
    """Converts and writes out LZ78 encoded version of s as 0 and 1 characters"""
    tree = {"": 0}
    s = ""

    for n, x in enumerate(stream):
        logging.info("READ: '"+x+"'")
        if (s+x) in tree:
            s = s + x
            continue
        
        # Write out the code for the new substring s+x and update tree
        tree[s+x] = pointer(tree, s, x)
        s = ""
    
    # Write out the last recorded prefix, pushing the last symbol out of the prefix s, if it is not empty.
    if s != "":
        x, s = s[-1], s[:-1]
        pointer(tree, s, x)

    #f = open('cipheredText', 'wb')
    #f.write()
    return tree

def pointer(lookup, prefix, symbol):
    """Write out the code for the substring prefix+symbol and return size of lookup"""
    n = len(lookup)                              
    i = int_to_bin(lookup[prefix], bits_for(n)) 
    logging.info("("+str(lookup[prefix])+","+symbol+") ["+str(bits_for(n))+" bits]")

    #sys.stdout.write(i + symbol_to_bin(symbol)) 
    return n

###################################################################################
def bits_for(n):
    """Compute number of bits to encode n"""
    if n == 1:
        return 1
    else:
        return int(math.ceil(math.log(n,2)))

def symbol_to_bin(c):
    """Convert an ASCII character c to 7 bits"""
    return int_to_bin(ord(c),7)

def int_to_bin(x,d):
    """Convert an integer x to d bits"""
    return ('{0:0'+str(d)+'b}').format(x)

###################################################################################
# Main
"""if __name__ == "__main__":
    # Uncomment line below to show encoding state
    # logging.basicConfig(level=logging.INFO)
    
    input_string = sys.stdin.read().strip()
    encode(input_string)"""