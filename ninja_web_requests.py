#!/usr/bin/env python3

import requests
import sys
import re

#Use with http://web-track-1.runcode.ninja/

def web_track(web_page):
        response=requests.get(web_page) #GET request for web page
        flag=re.findall('RCN{who_put_this_here}',response.text) #searches using regular expression for a flag
        if not flag: 
                return False #if match is empty, return False
        return flag #otherwise return the flag

def main():
        flag=web_track(sys.argv[1]) #sets return value to flag variable
        counter=1 #starts a counter to increment the pages
        while flag==False: 
                page=sys.argv[1]+'product/'+str(counter) #adds the product path to the web page and a counter that increments the pages.
                flag=web_track(page) 
                counter+=1 #increments web page
        return flag[0]



if __name__=="__main__":
        print(main())
