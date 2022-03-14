# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/24 20:45
"""
import sqlite3

con = sqlite3.connect("D:/sqlite3db/demo.db")
cur = con.cursor()
sql = "delete from t_person where pno=?"

try:
    cur.execute(sql, (1,))
    con.commit()
    print("删除成功")
except Exception as e:
    print(e)
    print("删除失败")
    con.rollback()
finally:
    cur.close()
    con.close()