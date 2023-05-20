# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/19 17:31
"""

import asyncio, time


async def do_work(x):
    print(f"waiting {x}")
    await asyncio.sleep(x)
    return f"done after {x} s"


async def main():
    # 创建多个协程对象
    # 封装任务列表
    coroutine1 = do_work(1)
    coroutine2 = do_work(2)
    coroutine3 = do_work(3)

    tasks = [asyncio.ensure_future(coroutine1),
             asyncio.ensure_future(coroutine2),
             asyncio.ensure_future(coroutine3)]

    # 获取协程返回结果的方式1
    # dones, pending = await asyncio.wait(tasks)
    # for task in dones:
    #     print(f"result: {task.result()}")

    # 获取协程返回结果的方式2
    # results = await asyncio.gather(*tasks)
    # for result in results:
    #     print(f"result: {result}")

    # 获取协程返回结果3
    return await asyncio.gather(*tasks)

start = time.time()
# 将main协程加入到事件循环当中
loop = asyncio.get_event_loop()
results = loop.run_until_complete(main())
for result in results:
    print(f"result: {result}")
print(f"running time: {time.time()-start} s")

