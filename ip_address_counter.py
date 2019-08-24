#!/usr/bin/env python

import sys
import re

# Uses regular expressions to match IP addresses and counts the total number in test file
# Use the test file ip_address_counter.txt

def display_IP(key, list_name):
    print key + ' - ' + str(list_name[key

def count_IPs(filename):
    file_content = open(filename, 'r')
    content = file_content.readlines()
    unique_ip = {}

    for line in content:
        match = re.findall(r'^[\d]{1,3}.[\d]{1,3}.[\d]{1,3}.[\d]{1,3}', line)
        match = ''.join(match) 
        if not match in unique_ip:
            unique_ip[match] = 1
        else: 
            unique_ip[match]+=1

    sorted_IP = sorted(unique_ip.keys())
    for key in sorted_IP:
        display_IP(key, unique_ip)


def main():
    first_arg = sys.argv[1]
    count_IPs(first_arg)


if __name__ == '__main__':
    main()
