# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/8 16:20
"""
import pickle

# 序列化
with open('../os_related/data.dat', 'wb') as f:
    a = "1"
    b = 1
    c =[1]

    pickle.dump(a, f)
    pickle.dump(b, f)
    pickle.dump(c, f)

# 反序列化
with open('../os_related/data.dat', 'rb') as f:
    a = pickle.load(f)
    b = pickle.load(f)
    c = pickle.load(f)

    print(a)
    print(b)
    print(c)
