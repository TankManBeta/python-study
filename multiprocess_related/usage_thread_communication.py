# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/2 21:06
"""
import time
from threading import *

# 定义全局变量
num = 10


def test1():
    global num
    for i in range(3):
        num += 1
    print(f"num1:{num}")


def test2():
    global num
    print(f"num2:{num}")


if __name__ == "__main__":
    # 同一个进程内的所有线程共享全局变量
    t1 = Thread(target=test1)
    t2 = Thread(target=test2)
    t1.start()
    t1.join()
    t2.start()
    t2.join()