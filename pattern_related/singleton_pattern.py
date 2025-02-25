# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/11/25 14:08
"""


class MySingleton:
    __obj = None
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)
        return cls.__obj

    def __init__(self, name):
        if MySingleton.__init_flag:
            print("init.....")
            self.name = name
            MySingleton.__init_flag = False


if __name__ == "__main__":
    a = MySingleton("aa")
    b = MySingleton("bb")