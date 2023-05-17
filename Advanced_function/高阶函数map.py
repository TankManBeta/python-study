# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/16 14:35
"""
from collections.abc import Iterator


def f(x):
    return x * x


nums = [1, 2, 3, 4, 5, 6]

nums_iter = map(f, nums)
print(f"是否是可迭代的对象：{isinstance(nums_iter, Iterator)}")
