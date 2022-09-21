# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/9/20 21:38
"""

import threading
import time


def func1(delay):
    print(f"{threading.current_thread().getName()} starts fun1")
    time.sleep(delay)
    print(f"{threading.current_thread().getName()} ends fun1")


def func2(delay):
    print(f"{threading.current_thread().getName()} starts fun2")
    time.sleep(delay)
    print(f"{threading.current_thread().getName()} ends fun2")


class MyThread(threading.Thread):
    def __init__(self, func, name, args):
        super().__init__(target=func, name=name, args=args)

    def run(self):
        self._target(*self._args)


if __name__ == "__main__":
    print("start process")
    t1 = MyThread(func1, "thread-1", (2,))
    t2 = MyThread(func2, "thread-2", (4,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
