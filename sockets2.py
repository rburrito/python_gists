#!/usr/bin/env python

import socket
import sys
import time

#Script that opens layer 3 socket and loops until full flag value is captured.

def connect_to_server():
    time.sleep(2)
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address=(sys.argv[1], int(sys.argv[2]))
    sock.connect(server_address)
    data = sock.recv(64)
    return data, sock 

def main():
    if len(sys.argv) < 3:
        exit('You need more arguments')

    data, sock = connect_to_server()
    sock.send('getkey 0\n')
    key=sock.recv(128)[13:].strip('\n')
    sock.close()
    ascii_code = 65
    character_set={}

    while ascii_code < 126:
        data, sock = connect_to_server()
        letter = chr(ascii_code)
        sock.send('givechar ' + letter + ' ' + key + '\n') 

        index = sock.recv(64).strip()
        print(index)
        if len(index) < 12:
            character_set[letter]=index
        sock.close()
        ascii_code+=1
    return character_set
      
print(main())
