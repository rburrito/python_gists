#!/usr/bin/env python

import sys

#Converts ASCII encoded characters from a file to words
#Use test file unicode_to_words.txt

def ordinary_words(filename):
    fileS = open(filename, 'r')
    content = fileS.read()
    new_content = content.split(" ")
    converted_str = ""
    for num_str  in new_content:
        if '\n' in num_str:
            num_str = num_str.rstrip('\n')
        char = chr(int(num_str))
        converted_str += char
    return converted_str
    
def main():
    first_arg = sys.argv[1]
    print(ordinary_words(first_arg))

if __name__ == '__main__':
    main()
