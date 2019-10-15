#!/usr/bin/env python3

import sys
import requests
import re

def blackjack(site, session):
        response=session.post(site, params={"do_what":"deal"}) #makes a POST request with the parameters "do_what" equal to deal
        win=re.findall("RCN{automate_the_boring_stuff}", response.text) #looks for the flag in the the text of the page.
        if not win:
                return False
        return win[0]

def main():
        session=requests.Session() #starts a new session
        get_req=session.get(sys.argv[1]) #uses this session to make a GET request
        site=sys.argv[1]+"bj.php" #after the first request, make POST requests to bj.php
        flag=blackjack(site, session) #Passes the session and site created in this function to the blackjack function
        while flag==False:
                flag=blackjack(site, session) #While flag is equal to False, keep making POST requests
        return flag


if __name__== "__main__":
        print(main())



