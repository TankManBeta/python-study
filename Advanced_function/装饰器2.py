# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/16 17:17
"""


def fun_out1(fun):
    print("装饰器1")

    def fun_in1():
        print("hello 1")
        fun()

    return fun_in1


def fun_out2(fun):
    print("装饰器2")

    def fun_in2():
        print("hello 2")
        fun()

    return fun_in2


@fun_out2
@fun_out1
def fun1():
    print("功能1")


fun1()
