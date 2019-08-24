#!/usr/bin/env python

#Use http://web-track-1.runcode.ninja/ as first_arg

import requests
import re
import sys

def track_web(count):
    first_arg = sys.argv[1]
    res = requests.get(first_arg + '/product/' + str(count))
    flag = re.findall(r'RCN{who_put_this_here}', res.text)

    if flag == []:
        return False
    return flag[0]

def main():
    first_arg = sys.argv[1]
    counter = 1

    while track_web(counter) == False:
        web_crawl=track_web(counter)
        counter+=1

    web_crawl = track_web(counter)
    if web_crawl:
        return web_crawl


if __name__ == '__main__':
    print(main())
