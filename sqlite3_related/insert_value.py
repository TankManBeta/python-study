# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/24 20:14
"""
import sqlite3

con = sqlite3.connect("D:/sqlite3db/demo.db")
cur = con.cursor()
sql = "insert into t_person(pname, age) values (?,?)"
try:
    cur.execute(sql, ("张三", 24))
    con.commit()
    print("Insert info successfully")
except Exception as e:
    print(e)
    con.rollback()
    print("Fail to insert info")
finally:
    cur.close()
    con.close()
