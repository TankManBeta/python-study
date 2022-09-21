# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/9/20 20:32
"""
from multiprocessing import *
from time import sleep


def write(q):
    a = ['a', 'b', 'c', 'd']
    for i in a:
        print(f"开始写入的值：{i}")
        q.put(i)
        sleep(1)


def read(q):
    for i in range(q.qsize()):
        print(f"读取到的值：{q.get()}")
        sleep(1)


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
