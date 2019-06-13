# -*- coding:UTF-8 -*-

import socket

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('198.87.90.222', 9021))
        msg = client.recv(1024)
        print('Receive message from server: %s' % msg)
    except Exception as e:
        print(e)
    finally:
        client.close()