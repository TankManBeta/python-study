# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/13 14:17
"""
from socket import *
from threading import Thread

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(('', 9988))


def recv_fun():
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(f">>{recv_data[1]}:{recv_data[0].decode('gb2312')}")


def send_fun():
    while True:
        addr = ("192.168.1.103", 9999)
        data = input("<<：")
        udp_socket.sendto(data.encode("gb2312"), addr)


if __name__ == "__main__":
    t1 = Thread(target=send_fun)
    t2 = Thread(target=recv_fun)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
