#!/usr/bin/python

import socket

def parseMsg(strMsg):
    _strMsg = strMsg.upper()
    msgArr = _strMsg.split(":")
    if(len(msgArr) < 2):
        print("Warn: Unkown message type!")
    else:
        val = float(msgArr[1])
        # print(f"{msgArr[0]}:{val}")
        ## runCtrlLogic(msgArr[0], msgArr[1]) # implemented directly below
        if(_strMsg.startswith("F")):
            print("F")
        elif(_strMsg.startswith("R")):
            print("R")
        elif(_strMsg.startswith("L")):
            print("L")
        else:
            print("Error: Unknown message head!")

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
        parseMsg(clientMsg) # exact logic for control
        # Send a reply to client
        msgFromServer       = "Client state running on: {}".format(address)
        bytesToSend         = str.encode(msgFromServer)
        UDPServerSocket.sendto(bytesToSend, address)


start_udp_server()
