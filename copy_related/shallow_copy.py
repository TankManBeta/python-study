# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/11/9 22:51
"""
import copy
a = [10, 20, [30, 40]]
b_shallow = copy.copy(a)

print("a:", a)
print("b_shallow:", b_shallow)

b_shallow.append(60)
b_shallow[2].append(70)
print("######浅拷贝后######")
print("a:", a)
print("b_shallow:", b_shallow)
