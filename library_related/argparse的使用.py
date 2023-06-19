# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/19 16:37
"""
import argparse

# 定义一个命令行解析对象
parser = argparse.ArgumentParser(description='demo')
# 添加命令行参数
parser.add_argument("--epochs", type=int, default=100)
parser.add_argument("--batch", type=int, default=4)
# 从命令行中结构化解析参数
args = parser.parse_args()
print(args)
