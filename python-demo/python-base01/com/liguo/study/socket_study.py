#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

from socket import *
from time import ctime

HOST = ''
PORT = 21576

BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True :
    print("waiting for connetion....")
    tcpCliSock, addr = tcpSerSock.accept()
    print("... connected from :", addr)
    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        print(" having.....")
    tcpCliSock.close()
tcpSerSock.close()