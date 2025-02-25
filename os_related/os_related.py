# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/16 15:41
"""
import os
from os import path
# 命令行
os.system("ping www.baidu.com")
# 打开外部程序
os.startfile(r"E:\Program Files\Tencent\QQ\Bin\QQScLauncher.exe")
# 文件和文件夹相关操作
print(os.name)
print(os.sep)
print(repr(os.linesep))
print(os.stat(r"../copy_related/deep_copy.py"))
# 工作目录相关操作
print(os.getcwd())
os.chdir(r"d:/")
os.mkdir(r"new_test")
os.rmdir(r"d:/new_test")
os.makedirs(r"test/test_sub")  # 目录不为空不能删除
os.removedirs(r"test/test_sub")
# os.path相关操作
print(path.isabs(r"d:/markdown_files/summary.md"))
print(path.isdir(r"d:/markdown_files/summary.md"))
print(path.isfile(r"d:/markdown_files/summary.md"))
print(path.exists(r"d:/markdown_files/summary.md"))
print(path.getsize(r"d:/markdown_files/summary.md"))
print(path.abspath(r"d:/markdown_files/summary.md"))
print(path.getctime(r"d:/markdown_files/summary.md"))
print(path.getatime(r"d:/markdown_files/summary.md"))
print(path.getmtime(r"d:/markdown_files/summary.md"))
# os.walk递归遍历所有子目录和子文件
cwd_path = os.getcwd()
list_files = os.walk(cwd_path)
for dir_path, dir_names, file_names in list_files:
    for dir in dir_names:
        print(path.join(dir_path, dir))
    for file in file_names:
        print(path.join(dir_path, file))
