# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/17 20:44
"""
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
# 绑定一个端口，ip一般不用写
s.bind(('', 9988))
addr = ("192.168.1.103", 9999)
data = input("请输入要发送的消息：")
s.sendto(data.encode("gb2312"), addr)
# 本次接受的最大字节数
re_data = s.recvfrom(1024)
print(re_data[0].decode("gb2312"))
s.close()
