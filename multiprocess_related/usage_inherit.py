# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/15 21:14
"""
# 继承Process类，同时重写run方法
from multiprocessing import Process
import time


class ClockProcess(Process):
    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        print(f"子进程开始执行的时间：{time.ctime()}")
        time.sleep(self.interval)
        print(f"子进程结束执行的时间：{time.ctime()}")


if __name__ == "__main__":
    print("主进程开始执行")
    p = ClockProcess(5)
    p.start()
    p.join()
    print("主进程执行完毕")
