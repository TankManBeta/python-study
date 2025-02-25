# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/1 20:51
"""


class Foo(object):
    def f1(self):
        print("original f1")

    def f2(self):
        print("original f2")


class FooDecorator(object):
    def __init__(self, decorator):
        self._decorator = decorator

    def f1(self):
        print("decorated f1")
        self._decorator.f1()

    def __getattr__(self, name):
        return getattr(self._decorator, name)


if __name__ == "__main__":
    u = Foo()
    v = FooDecorator(u)
    v.f1()
    v.f2()
