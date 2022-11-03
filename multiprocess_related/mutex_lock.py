# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/3 15:55
"""
from threading import *

# 定义全局变量
num = 0
# 创建互斥锁
lock = Lock()


def test1():
    global num
    # 上锁
    lock.acquire()
    for i in range(1000000):
        num += 1
    # 释放
    lock.release()
    print(f"num1:{num}")


def test2():
    global num
    # 上锁
    lock.acquire()
    for i in range(1000000):
        num += 1
    # 释放
    lock.release()
    print(f"num2:{num}")


if __name__ == "__main__":
    # 给全局变量上锁
    t1 = Thread(target=test1)
    t2 = Thread(target=test2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
