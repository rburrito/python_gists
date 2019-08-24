#!/usr/bin/env python

import sys
import requests

#Makes post request to website with initial value of "hashme". 
#Posts hash value to site until all characters from flag "RCN{573_still_using_urllib2}" display  

def make_requests(url1, url2, value):
    res1 = requests.post(url1, data={"food": value})
    res2 = requests.post(url2, data={"food":res1.content[13:-8]})
    data = ""

    while data != "RCN{573_still_using_urllib2}":
        res1 = requests.post(url1, data={"food": res2.content[13:-8]})
        res2 = requests.post(url2, data={"food": res1.content[13:-8]})
        if len(res1.content[13:-8]) < 64:
            data+=res1.content.rstrip('\n')
        elif len(res2.content[13:-8]) < 64:
            data+=res2.content.rstrip('\n')
    return data
        
def main():
    print(make_requests(sys.argv[1], sys.argv[2], sys.argv[3])

main()
