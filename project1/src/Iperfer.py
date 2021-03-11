#!/usr/bin/env python3

import socket 
import time
import sys

try:
    serverHostname = sys.argv[1]
    serverPort = sys.argv[2]
    seconds = sys.argv[3]
    serverAddress = (serverHostname, serverPort)
    seconds = int(seconds)
    serverPort = int(serverPort)
    t_end = time.time() + seconds
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if 1024>serverPort<65535:
        print('Error: port number must be in the range 1024 to 65535')
    else: 
        while time.time() < seconds:
            listen_socket.connect(serverAddress)
            data = listen_socket.recv(1024)
            buf = bytes(data, "utf-8") + b'\0'
            #data = listen_socket.recv(1024)
            listen_socket.sendall(buf) 
            listen_socket.close()
            print('sent='+len(buf)*1000 +' KB rate='+len(buf)/seconds)   
except:
    print('Error: missing or additional arguments')
