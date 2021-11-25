# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/11/8 23:45
"""
import io
s = "Hello, world!"
sio = io.StringIO(s)
print(sio.getvalue())
sio.seek(7)
sio.write('W')
print(sio.getvalue())