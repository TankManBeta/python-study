# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/19 18:28
"""
import asyncio,time


async def do_work(x):
    print(f"waiting:{x}")
    await asyncio.sleep(x)
    return f"Done after {x} s"


coroutine1 = do_work(1)
coroutine2 = do_work(2)
coroutine3 = do_work(3)
tasks = [asyncio.ensure_future(coroutine1),
         asyncio.ensure_future(coroutine2),
         asyncio.ensure_future(coroutine3)]
start = time.time()
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:
    print(asyncio.Task.all_tasks())
    for task in asyncio.Task.all_tasks():
        print(task.cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()
print(f"running time: {time.time()-start} s")
