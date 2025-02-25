# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/16 18:40
"""


def write_log(func):
    print(f"访问了方法：{func.__name__}")


def fun_out(func):
    def fun_in(x, y):
        write_log(func)
        return func(x, y)
    return fun_in


@fun_out
def add(a, b):
    return a + b


print(f"两数之和为{add(10, 20)}")
