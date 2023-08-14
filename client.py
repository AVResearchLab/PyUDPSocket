import socket

HOST = "127.0.0.1"
PORT = 9393
BUFFER  = 1024 

def client_program():
    client_socket = socket.socket()  # instantiate
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    while True:
        message = input(" -> ")  # again take input
        client_socket.sendto(message.encode(), (HOST, PORT))
        msgFromServer = client_socket.recvfrom(BUFFER)
        msg = "Message from Server: {}".format(msgFromServer[0].decode())
        print(msg)


if __name__ == '__main__':
    client_program()
