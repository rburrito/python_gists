#!/usr/bin/env python3

import sys
import requests
import re

#A script that finds the flag after winning a black jack game. 

def blackjack(site, session):
        response=session.post(site, params={"do_what":"deal"})
        win=re.findall("RCN{automate_the_boring_stuff}", response.text)
        if not win:
                return False
        return win[0]

def main():
        session=requests.Session()
        get_req=session.get(sys.argv[1])
        site=sys.argv[1]+"bj.php"
        flag=blackjack(site, session)
        while flag==False:
                flag=blackjack(site, session)
        return flag
                                

if __name__== "__main__":
        print(main())
