# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/17 15:24
"""
import re

# match方法
print("==============================")
s = "hello python hello"
pattern = "hello"
o = re.match(pattern, s)
print(o)
print(o.group())
print(o.span())
print(o.start())
print("============flags=============")
s = "hello python hello"
pattern = "Hello"
o = re.match(pattern, s, re.I)
print(o)
print(o.group())
print(o.span())
print(o.start())
