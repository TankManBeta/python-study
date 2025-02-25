# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/9/20 21:38
"""

import threading
import time


def func1(name, delay):
    print(f"{name} starts fun1")
    time.sleep(delay)
    print(f"{name} ends fun1")


def func2(name, delay):
    print(f"{name} starts fun2")
    time.sleep(delay)
    print(f"{name} ends fun2")


if __name__ == "__main__":
    print("start process")
    t1 = threading.Thread(target=func1, args=("thread1", 2))
    t2 = threading.Thread(target=func2, args=("thread2", 3))
    t1.start()
    t2.start()
    t1.join()
    t2.join()