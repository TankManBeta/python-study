# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/3 16:03
"""
from threading import Thread, Lock
import time

# 三把互斥锁
lock1 = Lock()
lock2 = Lock()
lock3 = Lock()
lock2.acquire()
lock3.acquire()


class Task1(Thread):
    def run(self) -> None:
        while True:
            if lock1.acquire():
                print("task1")
                time.sleep(2)
                lock2.release()


class Task2(Thread):
    def run(self) -> None:
        while True:
            if lock2.acquire():
                print("task2")
                time.sleep(2)
                lock3.release()


class Task3(Thread):
    def run(self) -> None:
        while True:
            if lock3.acquire():
                print("task3")
                time.sleep(2)
                lock1.release()


if __name__ == "__main__":
    t1 = Task1()
    t2 = Task2()
    t3 = Task3()
    t1.start()
    t2.start()
    t3.start()
