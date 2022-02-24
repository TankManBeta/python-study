# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/24 20:16
"""


import sqlite3

con = sqlite3.connect("D:/sqlite3db/demo.db")
cur = con.cursor()
sql = "insert into t_person(pname, age) values (?,?)"
try:
    cur.executemany(sql, [("李四", 23), ("王二麻子", 25)])
    con.commit()
    print("Insert info successfully")
except Exception as e:
    print(e)
    con.rollback()
    print("Fail to insert info")
finally:
    cur.close()
    con.close()
