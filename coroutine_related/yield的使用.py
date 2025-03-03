# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/19 15:24
"""


def foo():
    print("starting")
    while True:
        res = yield 4
        print("res:", res)


"""
在函数中使用了yield，则该函数就成为了一个生成器
yield的理解：
（1）当成return，程序返回
（2）当成生成器
"""
g = foo()
print(next(g))
print("*" * 20)
print(next(g))
