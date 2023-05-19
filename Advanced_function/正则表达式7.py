# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/18 11:39
"""
import re
print("================分组的使用===============")
# 匹配座机号码，区号{3,4}-电话号码{5,8}
pattern = r"(\d{3,4})-([1-9]\d{4,7}$)"
s = "010-1234567"
o = re.match(pattern, s)
print(o)
print(o.groups())
print(o.group(1))

# 匹配网页的标签数据
# pattern = r'<.+><.+>.+</.+></.+>'
pattern = r'<(.+)><(.+)>.+</\2></\1>'
s1 = "<html><head>这是head部分</head></html>"
o1 = re.match(pattern, s1)
print(o1)
s2 = "<html><head>这是head部分</head></body>"
o2 = re.match(pattern, s2)
print(o2)
# 分组起别名
pattern = r'<(?P<k_html>.+)><(?P<k_head>.+)>.+</(?P=k_head)></(?P=k_html)>'
s1 = "<html><head>这是head部分</head></html>"
o1 = re.match(pattern, s1)
print(o1)
s2 = "<html><head>这是head部分</head></body>"
o2 = re.match(pattern, s2)
print(o2)
