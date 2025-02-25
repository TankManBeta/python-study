# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/16 15:08
"""
nums = [-100, 100, 99, 2, 0, -20]
sorted_nums = sorted(nums)
print(f"默认升序：{sorted_nums}")

nums = [-100, 100, 99, 2, 0, -20]
sorted_nums = sorted(nums, reverse=True)
print(f"使用reverse降序：{sorted_nums}")

nums = [-100, 100, 99, 2, 0, -20]
sorted_nums = sorted(nums, key=abs)
print(f"按绝对值排序：{sorted_nums}")
