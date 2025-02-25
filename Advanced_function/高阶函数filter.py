# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/16 14:56
"""


def is_odd(x):
    return x % 2 == 0


nums = [1, 2, 3, 4, 5, 6]
print(list(filter(is_odd, nums)))
