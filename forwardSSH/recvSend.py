# -*- coding: utf-8 -*-
from socket import *
import threading
import time

buffer_size = 2048

def server(host, port):
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(10)
    server_socket, address = server_socket.accept()

    while True:
        data = server_socket.recv(buffer_size)
        if len(data):
            print "server recv:" + str(data)
            data = server_socket.send(data)
        time.sleep(1)


def client(ip, port):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((ip, port))

    for i in range(10):
        try:
            data = "send number is " + str(i)
            data = client_socket.send(data)
            data = client_socket.recv(buffer_size)
            if len(data):
                print "client recv:" + str(data)
            time.sleep(1)
        except:
            pass



if __name__ == "__main__":
    print("start recv and send...")

    #t = threading.Thread(target=server, args=('0.0.0.0', 8102))
    #t.start()

    client('localhost', 8102)