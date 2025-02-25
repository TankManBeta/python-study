# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/2 21:06
"""
from threading import *

# 定义全局变量
num = 0


def test1():
    global num
    for i in range(1000000):
        num += 1
    print(f"num1:{num}")


def test2():
    global num
    for i in range(1000000):
        num += 1
    print(f"num2:{num}")


if __name__ == "__main__":
    # 同一个进程内的所有线程共享全局变量存在问题，当一个线程的占有的时间片不足以执行自己想要的操作（比如全局变量+1）时，另一个线程抢占
    # cpu执行操作，使得全局变量+1，第一个进程会在第一个基础之上+1而不是第二个基础之上+1
    t1 = Thread(target=test1)
    t2 = Thread(target=test2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
