# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/18 16:03
"""
import re
print("==============================贪婪模式===============================")
v = re.match(r'(.+)(\d+-\d+-\d+)', "this is my tel:133-1234-1234")
print(v.group(1))
print(v.group(2))
print("==============================非贪婪模式===============================")
v = re.match(r'(.+?)(\d+-\d+-\d+)', "this is my tel:133-1234-1234")
print(v.group(1))
print(v.group(2))
