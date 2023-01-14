# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/3 19:12
"""
import threading

local = threading.local()


def process_student():
    student_name = local.name
    print(f"Thread:{threading.current_thread().getName()} Name:{student_name}")


def process_thread(name):
    # 将传入的name值绑定到local的name上
    local.name = name
    process_student()


t1 = threading.Thread(target=process_thread, args=("a",), name="ThreadA")
t2 = threading.Thread(target=process_thread, args=("b",), name="ThreadB")
t1.start()
t2.start()
t1.join()
t2.join()
