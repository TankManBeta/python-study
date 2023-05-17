# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/16 16:49
"""
import time


def write_log(func):
    try:
        file = open("decorator.txt", 'a', encoding="utf-8")
        file.write("访问：")
        file.write(func.__name__)
        file.write("\t")
        file.write("时间：")
        file.write(time.asctime())
        file.write("\n")
    except Exception as e:
        print(e.args)
    finally:
        file.close()


def fun_out(func):
    def fun_in():
        write_log(func)
        func()

    return fun_in


# 相当于fun_out(fun1)
@fun_out
def fun1():
    print("功能1")


@fun_out
def fun2():
    print("功能2")


fun1()
