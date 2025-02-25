# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/19 17:24
"""
import asyncio,time


async def do_work(x):
    print(f"waiting:{x}")
    await asyncio.sleep(x)
    return f"Done after {x} s"

start = time.time()
coroutine1 = do_work(1)
coroutine2 = do_work(2)
coroutine3 = do_work(3)

tasks = [asyncio.ensure_future(coroutine1),
         asyncio.ensure_future(coroutine2),
         asyncio.ensure_future(coroutine3)]

# 创建事件循环
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print(f"task result:{task.result()}")
print(f"running time:{time.time()-start}")
