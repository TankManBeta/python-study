# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/9/20 20:12
"""
from multiprocessing import Process
num = 10


def work1():
    global num
    num += 5
    print("子进程1执行后num的值:", num)


def work2():
    global num
    num += 10
    print("子进程2执行后num的值:", num)


if __name__ == "__main__":
    # 子进程不共享全局变量的值
    print("主进程开始运行")
    p1 = Process(target=work1)
    p2 = Process(target=work2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("全局变量num的值为：", num)
