#!/usr/bin/env python3

import sys
import requests
import re

#A script that finds the flag after winning a game of black jack.
#Use with site https://learn.fullstackacademy.com/workshop/5d9776d693bae000044d7ed0/content/5da0980a90e5b80004593dd3/text

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
