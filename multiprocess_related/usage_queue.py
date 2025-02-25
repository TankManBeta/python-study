# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/9/20 20:21
"""

from multiprocessing import Queue

q = Queue(3)
# 向队列插入元素
q.put("消息1")
q.put("消息2")
q.put("消息3")
# put方法中可选参数 block=True, timeout=1 队列已经满了，等待1秒，如果还是没有空余空间，则抛出队列已满的异常
# q.put("消息4", block=True, timeout=1)
# 判断当前队列是否已满
print("当前队列是否已满：", q.full())
if not q.full():
    q.put("消息4", block=True, timeout=1)

# 读取并删除元素
print(q.get())
print(q.get())
print(q.get())
# get方法中可选参数，如果队列已空，则抛出队列已空异常
# print(q.get(block=True, timeout=1))
if not q.empty():
    print(q.get(block=True, timeout=1))

# 查看队列的大小
print("队列的长度为：", q.qsize())
