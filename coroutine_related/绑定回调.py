# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/19 17:07
"""

import time, asyncio


async def do_work(x):
    print(f"waiting:{x}")
    return f"Done after {x} s"


# 定义回调函数
def callback(future):
    print(f"Callback:{future.result()}")


# 获取协程对象
coroutine = do_work(3)
# 创建事件循环
loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)
# 给任务添加绑定函数
task.add_done_callback(callback)
loop.run_until_complete(task)
