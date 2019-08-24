#!/usr/bin/env python

import sys

#Convert sample file with binary on each line to base 10
#Use test file binary_mafs.txt
#Sample input file might look like this:
# 0b1 0b10 0b11 0b100 0b101
# 0b1 0b11 0b111 0b1111 0b11111
#Sample output will look like this:
# 15
# 57

def binary_mafs(filename):
    fil3 = open(filename, 'r')
    content = fil3.readlines()
    for line in content:
        line = line.rstrip('\n')
        line = line.split(' ')
        sum = 0
        for binary in line:
            sum+=int(binary, 2)
        print(sum)

def main():
    first_arg = sys.argv[1]
    binary_mafs(first_arg)

if __name__ == '__main__':
    main()
