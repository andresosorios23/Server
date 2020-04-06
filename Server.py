import socket
import numpy as np
import struct
from time import sleep
import csv

localIP     = "192.168.1.2"
localPort   = 20001
bufferSize  = 1024
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
# Listen for incoming datagrams
bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
message = bytesAddressPair[0]
address = bytesAddressPair[1]
print(address)
while(True):
    f = open('log.txt','a')
    timestamp = str(UDPServerSocket.recvfrom(bufferSize)[0]).replace("'",'').replace('b','').replace('\\n','\r\n')
    values = str(UDPServerSocket.recvfrom(bufferSize)[0]).replace("'",'').replace('b','').replace('\\n','\r\n')
    print(timestamp)
    print(values)
    f.write(timestamp)
    f.write(values)
    sleep(0.7)
    f.close()


