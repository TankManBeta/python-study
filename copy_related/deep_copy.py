# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/11/11 14:33
"""
import copy
a = [10, 20, [30, 40]]
b_deep = copy.deepcopy(a)

print("a:", a)
print("b_deep:", b_deep)

b_deep.append(60)
b_deep[2].append(70)
print("######深拷贝######")
print("a:", a)
print("b_deep:", b_deep)
