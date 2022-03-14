# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/24 20:37
"""
import sqlite3

con = sqlite3.connect("D:/sqlite3db/demo.db")
cur = con.cursor()
sql = "update t_person set pname=? where pno=?"

try:
    cur.execute(sql, ("小张", 1))
    con.commit()
    print("修改成功")
except Exception as e:
    print(e)
    print("修改失败")
    con.rollback()
finally:
    cur.close()
    con.close()
