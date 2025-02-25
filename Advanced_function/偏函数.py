# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/16 19:11
"""
from functools import partial

new_int = partial(int, base=2)
print(new_int("10"))
print(new_int("1010"))
print(new_int("101010"))
