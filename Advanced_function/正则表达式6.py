# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/18 11:12
"""
import re
s = "I love python"
pattern = "love"
o1 = re.search(pattern, s)
print(o1)
o2 = re.match(pattern, s)
print(o2)

pattern = "aa|bb|cc"
s = "aa"
o = re.match(pattern, s)
print(o)

# 匹配0-100的所有数字
pattern = r"[1-9][0-9]$|100$"
s = "123"
o = re.match(pattern, s)
print(o)