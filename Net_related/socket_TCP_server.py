# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/13 16:13
"""
from socket import *
# 创建服务器端套接字对象
server_socket = socket(AF_INET, SOCK_STREAM)
# 绑定端口
server_socket.bind(('', 8989))
# 监听
server_socket.listen()
# 接收客户端发送的消息
client_socket, client_info = server_socket.accept()
recv_data = client_socket.recv(1024)
print(f"接收到{client_info}的消息{recv_data.decode('gb2312')}")
# 关闭连接
client_socket.close()
server_socket.close()
