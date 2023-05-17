# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/16 15:41
"""
import math


def fun_out(num1):
    def fun_in(num2):
        return num1 + num2

    return fun_in


f = fun_out(100)
res = f(200)
print(f"两个数的和为{res}")


def get_dist_out(x1, y1):
    def get_dist_in(x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return get_dist_in


f = get_dist_out(0, 0)
res = f(2, 2)
print(f"距离为{res}")
