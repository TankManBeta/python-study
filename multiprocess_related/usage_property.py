# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/15 20:57
"""
from multiprocessing import Process
from time import sleep


def worker(interval):
    print("work start")
    sleep(interval)
    print("work end")


if __name__ == "__main__":
    # 主进程等子进程执行完再继续执行后面的代码
    print("主进程正在执行")
    p = Process(target=worker, args=(3,))
    print(p.name)
    p.start()
    p.join()
    print("主进程执行完毕")
    print(p.is_alive())


