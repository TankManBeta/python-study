# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2024/5/22 23:01
"""

from __future__ import print_function

import grpc

import hello_pb2
import hello_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = hello_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(hello_pb2.HelloRequest(name='goodspeed'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
