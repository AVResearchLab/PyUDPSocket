# PyUDPSocket
Stores here are the simple scripts for making network connection using UDP socket via Python inner APIs.

<br>

Here is a simple utility of the 2 scripts:
*Server side*
```python
#!/usr/bin/python

import rospy
import socket
import math
from geometry_msgs.msg import Twist


HOST = "127.0.0.1"
PORT = 5566
BUFFER  = 1024 
cmd = Twist()


# Documentation
'''
1. Move with the speed of 2 in the direction of x:
linear: 
  x: 2.0
  y: 0.0
  z: 0.0

2. Rotation by Z-axis by 1.5 radians in plane:
angular: 
  x: 2.0
  y: 0.0
  z: 0.0

'''


def main():
    cmd_publisher = rospy.Publisher("/agent1/cmd_vel", Twist, queue_size=10)
    rospy.init_node('logi_control')

    rate = rospy.Rate(10)

    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((HOST, PORT))
    print("UDP server up and listening")
    while not rospy.is_shutdown():
        cmd_publisher.publish(cmd)
        rate.sleep()
        bytesAddressPair = UDPServerSocket.recvfrom(BUFFER)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = message.decode()
        _clientMsg = "Message from Client: {}".format(clientMsg)
        # _clientIP  = "Client IP Address: {}".format(address)
        print(_clientMsg)
        # print(_clientIP)
        msgFromServer       = "Client state running on: {}".format(address)
        bytesToSend         = str.encode(msgFromServer)
        UDPServerSocket.sendto(bytesToSend, address)
        ## Exact logic for control
        _strMsg = clientMsg.upper()
        msgArr = _strMsg.split(":")
        if(len(msgArr) < 2):
            print("Warn: Unkown message type!")
        else:
            key = msgArr[0]
            val = float(msgArr[1])
            print(f"{key}:{val}")
            ## runCtrlLogic(msgArr[0], msgArr[1]) # implemented directly below
            if(key == "F"):
                print("Move forward...")
                cmd.linear.x = val
            elif(key == "B"):
                print("Move backward...")
                cmd.linear.x = 0 - val
            elif(key == "R"):
                print("Move to the right...")
                cmd.angular.z = val
            elif(key == "L"):
                print("Move to the left...")
                cmd.angular.z = math.pi - val
            elif(key == "S"):
                print("Stop")
                cmd.linear.y = 0
            else:
                print("Error: Unknown message head!")

    print("Returned...")


if __name__ == '__main__':
    main()
```

*Client side*
```python
import socket

HOST = "127.0.0.1"
PORT = 5566
BUFFER  = 1024 

def client_program():
    client_socket = socket.socket()  # instantiate
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    while True:
        message = input(" -> ")  # again take input
        client_socket.sendto(message.encode(), (HOST, PORT))
        msgFromServer = client_socket.recvfrom(BUFFER) # WAITING THE SERVER'S RESPONSE!!!
        msg = "Message from Server: {}".format(msgFromServer[0].decode())
        print(msg)


if __name__ == '__main__':
    client_program()
```
