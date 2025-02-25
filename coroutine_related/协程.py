# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/19 16:31
"""
import asyncio
import time

now = lambda: time.time()


async def do_work(x):
    print(f"waiting:{x}")

start = now()
loop = asyncio.get_event_loop()
loop.run_until_complete(do_work(6))
end = now()
print(f"running time:{end-start}")