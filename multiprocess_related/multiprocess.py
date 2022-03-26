# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/26 15:46
"""
from multiprocessing import Process
import time


def run_test(name, **kwargs):
    for i in range(3):
        print("......sub......")
        print(f"name:{name}")
        print(f"dict:{kwargs}")
        time.sleep(3)


if __name__ == "__main__":
    print("......main......")
    p = Process(target=run_test, args=("aaa",), kwargs={"bbb": "ccc"})
    p.start()
