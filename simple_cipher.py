#!/usr/bin/env python

import sys

#Takes the first word of every sentence to create a coded message.
#Use test file simple_cipher.txt

def simple_cipher(filename):
    fil3 = open(filename, 'r')
    content = fil3.read()
    content = content.split('. ')
    decoded_message = []
    for line in content: 
        line = line.split(' ')
        decoded_message.append(line[0])
    print(' '.join(decoded_message))


def main():
    first_arg = sys.argv[1]
    simple_cipher(first_arg)
