#!/usr/bin/env python

import sys

# Convert hex values in file to numbers
# Use test file hex_mafs.txt
# Sample input file might contain this:
# 0x539 0x539
# 0x7a69 0x7a69
# Sample output file may look like this: 
# 2674
# 62674

def hex_mafs(filename):
    fil3 = open(filename, 'r')
    content = fil3.readlines()
    for line in content:
        line = line.rstrip('\n')
        line = line.split(' ')
        sum1 = 0
        for hex_value in line:
            sum1+=int(hex_value, 16)
        print(sum1)

def main():
    first_arg = sys.argv[1]
    hex_mafs(first_arg)


if __name__ == '__main__':
    main()
