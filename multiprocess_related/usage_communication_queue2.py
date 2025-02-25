# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/9/20 20:49
"""
from multiprocessing import Pool, Manager
from time import sleep


# 如果采用Pool创建进程，就需要使用mutliprocessing.Manager()中的Queue()来完成进程间的通信，而不是multiprocessing.Queue()，否则会抛出异常

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
    q = Manager().Queue()
    pool = Pool(3)
    pool.apply(write, (q,))
    pool.apply(read, (q,))
    pool.close()
    pool.join()
