# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/9/20 21:30
"""
import _thread
import time


def func1(name):
    print(f"开始运行{name}")
    time.sleep(4)
    print(f"结束运行{name}")


def func2(name):
    print(f"开始运行{name}")
    time.sleep(2)
    print(f"结束运行{name}")


if __name__ == "__main__":
    print("开始运行")
    _thread.start_new_thread(func1, ("Process-1",))
    _thread.start_new_thread(func2, ("Process-2",))
    time.sleep(7)
