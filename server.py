#!/usr/bin/python

import socket

def start_udp_server():
    HOST = "127.0.0.1"
    PORT = 9393
    BUFFER  = 1024 
    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Bind to address and ip
    UDPServerSocket.bind((HOST, PORT))
    print("UDP server up and listening")
    # Listen for incoming datagrams
    while(True):
        bytesAddressPair = UDPServerSocket.recvfrom(BUFFER)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = message.decode()
        _clientMsg = "Message from Client: {}".format(clientMsg)
        _clientIP  = "Client IP Address: {}".format(address)
        print(_clientMsg)
        print(_clientIP)
        # Sending a reply to client
        msgFromServer       = "Client state running on: {}".format(address)
        bytesToSend         = str.encode(msgFromServer)
        UDPServerSocket.sendto(bytesToSend, address)


start_udp_server()
