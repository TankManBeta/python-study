# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/16 16:45
"""
import shutil
import zipfile

shutil.copy("data.dat", "data_copy.dat")
# 新建目录如果已存在则会报错
shutil.copytree("test_dir", "test_dir1", ignore=shutil.ignore_patterns("*.html"))
# 压缩、解压缩
shutil.make_archive("test_archive", "zip", "./test_dir")

z1 = zipfile.ZipFile("a.zip", "w")
z1.write(r"./os_related.py")
z1.write("./data.dat")
z1.close()