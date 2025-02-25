# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/16 14:47
"""
from functools import reduce


def f(x, y):
    return x + y


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = reduce(f, a)
print(total)
