# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/18 15:14
"""
import re

print("=====================sub和subn========================")
# 将phone中的注释去掉
phone = "010-234567-78979 # 这是一个电话号码"
pattern = r"#.*$"
res = re.sub(pattern, '', phone)
print(res)
res = re.subn(pattern, '', phone)
print(res)

print("=====================compile========================")
s = "first123 line"
pattern = r"\w+"
regex = re.compile(pattern)
res = regex.match(s)
print(res)

print("=====================findall========================")
s = "first 1 second 2 third 3"
pattern = r"\w+"
res = re.findall(pattern, s)
print(res)

print("=====================finditer========================")
s = "first 1 second 2 third 3"
pattern = r"\w+"
res = re.finditer(pattern, s)
for o in res:
    print(o)

print("=====================split========================")
s = "first 11 second 22 third 33"
pattern = r"\d+"
res = re.split(pattern, s)
print(res)
res = re.split(pattern, s, 1)
print(res)
