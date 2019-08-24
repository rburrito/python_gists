#!/usr/bin/env python

import sys
import binascii

# Converts unicode code points (hexadecimal strings) to raw strings 
# Use test file ASCII_stuffs.txt
# Sample input file might look like this: 
# 41 42 43 44 3f 0a 41 20 42 20 43 20 44 21
# Sample output: 
# ABCD?
# A B C D! 

def convert_to_ASCII(filename):
    fil3 = open(filename, 'r')
    content = fil3.read()

    content1 = content.rstrip('\n').split(" ")
    content1 = ''.join(content1)
    return binascii.a2b_hex(content1)

def main():
    first_arg = sys.argv[1]
    print(convert_to_ASCII(first_arg))

if __name__ == '__main__':
    main()
