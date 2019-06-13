# -*- coding: utf-8 -*-
from socket import *
import threading
import Queue

# test in python 2.7

# a dic of local port mapped to machine
ssh_server_dic = {"host": 'localhost', "port": 0, "ip": "x.x.x.x"}

# sync all the threads in each of tunnel
running_flag = []

# receive buffSize
buffer_size = 2048

def data_encryp(data):
    temp_data = list(data)
    for i in range(0, len(temp_data)):
        if ord(temp_data[i]) == 255:
            temp_data[i] = chr(0)
        else:
            temp_data[i] = chr(ord(temp_data[i]) + 1)
    return "".join(temp_data)

def data_decryp(data):
    temp_data = list(data)
    for i in range(0, len(temp_data)):
        if ord(temp_data[i]) == 0:
            temp_data[i] = chr(255)
        else:
            temp_data[i] = chr(ord(temp_data[i]) - 1)
    return "".join(temp_data)

def get_data_from_ssh_server(rev_msg, tcp_socket, flag):
    """
    :param rev_msg: a queue buffer of message need to be send to SSH client
    :param tcp_socket: instance of socket used for sending data
    :param flag: control this function
    :return: null
    """
    while running_flag[flag]:
        data = tcp_socket.recv(buffer_size)
        if len(data):
            rev_msg.put(data_decryp(data))
        else:
            running_flag[flag] = False


def send_data_to_ssh_client(rev_msg, tcp_socket, flag):
    """
    :param rev_msg: a queue buffer of message need to be send to SSH client
    :param tcp_socket: instance of socket used for sending data
    :param flag: control this function
    :return: null
    """
    while running_flag[flag]:
        try:
            data = rev_msg.get(timeout=10)
            data = tcp_socket.send(data_encryp(data))
        except:
            pass


def get_data_from_ssh_client(send_msg, tcp_socket, flag):
    """
    :param send_msg: a queue buffer of message need to be send to SSH server in each machine
    :param tcp_socket: instance of socket used for sending data
    :param flag: control this function
    :return: null
    """
    while running_flag[flag]:
        data = tcp_socket.recv(buffer_size)
        if len(data):
            send_msg.put(data_decryp(data))
        else:
            running_flag[flag] = False


def send_data_to_ssh_server(send_msg, tcp_socket, flag):
    """
    :param send_msg: a queue buffer of message need to be send to SSH server in each machine
    :param tcp_socket: instance of socket used for sending data
    :param flag: control this function
    :return: null
    """
    while running_flag[flag]:
        try:
            data = send_msg.get(timeout=10)
            data = tcp_socket.send(data_encryp(data))
        except:
            pass


def handle_connections(host, ip, port):
    """
    :param host: local ip
    :param ip: which machine the data will be forwarded
    :param port: local port
    :return: null
    """
    ssh_client_socket = socket(AF_INET, SOCK_STREAM)
    ssh_client_socket.bind((host, port))

    # listen 10 client
    ssh_client_socket.listen(10)
    while True:
        ssh_client_side, address = ssh_client_socket.accept()

        # two queue for keeping data from SSH client and SSH server
        buffer_send = Queue.Queue()
        buffer_rev = Queue.Queue()

        ssh_server_side = socket(AF_INET, SOCK_STREAM)
        ssh_server_side.connect((ip, 2222))

        flag = True

        running_flag.append(flag)

        rev1 = threading.Thread(target=get_data_from_ssh_server,
                                args=(buffer_rev, ssh_server_side, len(running_flag) - 1))
        rev2 = threading.Thread(target=send_data_to_ssh_client,
                                args=(buffer_rev, ssh_client_side, len(running_flag) - 1))

        send1 = threading.Thread(target=get_data_from_ssh_client,
                                 args=(buffer_send, ssh_client_side, len(running_flag) - 1))
        send2 = threading.Thread(target=send_data_to_ssh_server,
                                 args=(buffer_send, ssh_server_side, len(running_flag) - 1))

        rev1.start()
        rev2.start()
        send1.start()
        send2.start()


if __name__ == "__main__":
    print("start SSH forward server")

    print("ssh mapping " + ssh_server_dic["host"] + ":" + str(ssh_server_dic["port"]) + " => " + ssh_server_dic["ip"] + ":22")
    t = threading.Thread(target=handle_connections, args=(ssh_server_dic["host"], ssh_server_dic["ip"], ssh_server_dic["port"]))
    t.start()

    print("initialize SSH forward server done")
