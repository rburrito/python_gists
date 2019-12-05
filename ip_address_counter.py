#/usr/bin/env python3

import sys
import re
# Uses regular expressions to match IP addresses and counts the frequency of appearance
# Use the test file ip_address_counter.txt

def display_IP(key, list_name):
    return key + ' - ' + str(list_name[key])

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
    new_list=[]
    for key in sorted_IP:
        new_list.append(display_IP(key, unique_ip))

    return new_list

def main():
    first_arg = sys.argv[1]
    print(*count_IPs(first_arg), sep='\n')


if __name__ == '__main__':
    main()
