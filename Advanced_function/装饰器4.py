# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/16 18:57
"""
import time


def write_log(func):
    print(f"于{time.asctime()}调用了函数{func.__name__}")


def fun_out(func):
    def fun_in(*args, **kwargs):
        write_log(func)
        return func(*args, **kwargs)

    return fun_in


@fun_out
def add(a, b):
    return a + b


@fun_out
def minus(a, b, c):
    return a - b - c


print(f"两数之和为{add(10, 20)}")
print(f"三数之差为{minus(10, 20, 30)}")
