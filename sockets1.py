#!/usr/bin/env python

import sys
import socket

def main():

    if len(sys.argv) < 3:
        exit('You did not provide the arguments!')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (sys.argv[1],int(sys.argv[2])) 
#sys.argv[1] is IP address; sys.argv[2] is port number

    sock.connect(server_address)

    data = sock.recv(1)
    print(data.rstrip('\n'))
    print("Data just received") 
    index = 0
    
    while data != '}':
        print("In while loop")
        sock.send('givechar ' + str(index)+'\n')
        print('Just sent a char')
        data = sock.recv(1024) #default is usually 1024
        print('Just received some cool stuff ' + data)
        index+=1
    print(data)
    sock.close()

main()
