# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/17 16:47
"""
import re

print("=================*的使用=================")
s = "123qwe"
pattern = "\d*"
o = re.match(pattern, s)
print(o)
print("=================+的使用=================")
s = "a123qwe"
pattern = "\d+"
o = re.match(pattern, s)
print(o)
print("=================?的使用=================")
s = "a123qwe"
pattern = "\d?"
o = re.match(pattern, s)
print(o)
print("================={m}的使用=================")
s = "123qwe"
pattern = "\d{2}"
o = re.match(pattern, s)
print(o)
print("================={m,n}的使用=================")
s = "123456qwe"
pattern = "\d{2,5}"
o = re.match(pattern, s)
print(o)
print("================={m,}的使用=================")
s = "123456qwe"
pattern = "\d{2,}"
o = re.match(pattern, s)
print(o)
