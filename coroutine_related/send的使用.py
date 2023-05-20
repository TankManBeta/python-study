# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/19 16:00
"""


def foo():
    print("starting")
    while True:
        res = yield 4
        print(f"res:{res}")


g = foo()
print(next(g))
print(g.send(10))
