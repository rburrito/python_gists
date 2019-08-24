#!/usr/bin/env python

import sys

#Takes a file with words on multiple lines into one long string separated by ' '
#Use test file lines_manipulation.txt

def make_one_line(filename):
    file1 = open(filename, 'r')
    content = file1.readlines()
    new_content = ""
    for num, line in enumerate(content, start=1):
        new_content += line.replace('\n', ' ')

    new_content_list = new_content.split(' ')
    
    good_content = []
    for string in new_content_list:
        if string!='':
            good_content.append(string)
    print(' '.join(good_content))

def main():
    first_arg=sys.argv[1]
    make_one_line(first_arg)

if __name__ == '__main__':
    main()
