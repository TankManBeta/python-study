# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/18 10:51
"""
import re
print("===============$的使用=================")
# 匹配5-10位的QQ邮箱，开头数字不能是0
pattern = r"[1-9]\d{4,9}@qq.com$"
# 可以匹配
# qq = r"12345@qq.com"
# 不可以匹配
qq = r"12345@qq.com.126.com"
o = re.match(pattern, qq)
print(o)

print("===============^的使用=================")
pattern = r"^hello"
s = r"hello python"
o = re.match(pattern, s)
print(o)

print(r"===============\b左边界的使用=================")
pattern = r".*\bhello"
s = r"python hello python"
o = re.match(pattern, s)
print(o)

print(r"===============\b右边界的使用=================")
pattern = r".*python\b"
s = r"python hello python"
o = re.match(pattern, s)
print(o)

print(r"===============\B非单词边界的使用=================")
pattern = r".*python\B"
s = r"hello pythonhello"
o = re.match(pattern, s)
print(o)
