# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/24 20:25
"""
import sqlite3

con = sqlite3.connect("D:/sqlite3db/demo.db")
cur = con.cursor()
sql = "select * from t_person"
try:
    cur.execute(sql)
    person_all = cur.fetchall()
    for person in person_all:
        print(person)
except Exception as e:
    print(e)
    print("查询失败")
finally:
    cur.close()
    con.close()
