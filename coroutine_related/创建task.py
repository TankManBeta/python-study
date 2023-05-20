# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/19 16:38
"""
import asyncio


async def do_work(x):
    print(f"waiting:{x}")


coroutine = do_work(3)
loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
# 创建任务的方式1
# task = asyncio.ensure_future(coroutine)
# loop.run_until_complete(task)
# 创建任务的方式2
task = loop.create_task(coroutine)
loop.run_until_complete(task)
