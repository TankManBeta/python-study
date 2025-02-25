# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/24 19:40
"""
import sqlite3

# 创建连接
con = sqlite3.connect("D:/sqlite3db/demo.db")
print(con)
# 创建游标对象
cur = con.cursor()
# 创建表的sql语句
sql = "create table t_person(pno INTEGER  primary key autoincrement, pname VARCHAR not null, age INTEGER )"
# 执行sql语句
try:
    cur.execute(sql)
    print("创建表成功")
except Exception as e:
    print(e)
    print("创建表失败")
# 关闭连接
finally:
    cur.close()
    con.close()
