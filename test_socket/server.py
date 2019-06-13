# -*- coding:UTF-8 -*-

import socket
import time

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('198.87.90.222', 9021))
    server.listen()
    print('Start listening at %s:%d' % ('198.87.90.222', 9021))
    stop = False
    while not stop:
        try:
            client_sock, client_address = server.accept()
            print('Receive client connection: %s:%d' % client_address)
            msg = 'Welcome %s:%d' % client_address
            send_len = client_sock.send(bytes(msg, 'utf-8'))
            if send_len != len(bytes(msg, 'utf-8')):
                print('Send to client (%s:%d) error!' % client_address)
            else:
                print('Send message (%s) to client ok!' % msg)
        except KeyboardInterrupt as e:
            print('Interrupted by user!')
            stop = True
        except Exception as e:
            print(e)
        finally:
            client_sock.close()
            time.sleep(1)
    server.close()
