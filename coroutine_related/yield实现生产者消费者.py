# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/19 16:03
"""


def produce(c):
    for i in range(1, 11):
        print(f"生产者生产产品：{i}")
        c.send(i)


def consumer():
    while True:
        res = yield
        print(f"消费者消费产品：{res}")


g = consumer()
next(g)
produce(g)
