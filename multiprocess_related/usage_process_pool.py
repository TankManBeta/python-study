# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/9/20 19:55
"""

import multiprocessing
import time


def func(msg):
    print("start:", msg)
    time.sleep(3)
    print("end:", msg)


if __name__ == "__main__":
    pool = multiprocessing.Pool(3)
    # 添加任务
    for i in range(5):
        msg = f"Task{i+1}"
        # 非阻塞
        pool.apply_async(func, (msg,))
        # 阻塞，类似单进程，前一个执行完才能执行后一个
        # pool.apply(func, (msg,))
    # 如果进程池不再接收新的请求，调用close
    pool.close()
    # 等待子进程结束之后主进程结束
    pool.join()
