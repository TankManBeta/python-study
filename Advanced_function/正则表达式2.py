# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/17 16:48
"""
import re

print("=================.的使用==================")
s = 'a'
pattern = '.'
o = re.match(pattern, s)
print(o)
print("=================\d的使用=================")
s = '0'
pattern = "\d"
o = re.match(pattern, s)
print(o)
print("=================\D的使用=================")
s = '-'
pattern = "\D"
o = re.match(pattern, s)
print(o)
print("=================\s的使用=================")
s = '\n'
pattern = "\s"
o = re.match(pattern, s)
print(o)
print("=================\S的使用=================")
s = '9'
pattern = "\S"
o = re.match(pattern, s)
print(o)
print("=================\w的使用=================")
s = 'l'
pattern = "\w"
o = re.match(pattern, s)
print(o)
print("=================\W的使用=================")
s = '+'
pattern = "\W"
o = re.match(pattern, s)
print(o)
print("=================[]的使用=================")
s = '2'
pattern = "[2468]"
o = re.match(pattern, s)
print(o)
