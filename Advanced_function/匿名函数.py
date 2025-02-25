# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/16 15:26
"""
f = lambda x, y, z: x + y + z
print(f(2, 3, 4))

nums = [1, 3, 5, 7, 9]
print(list(map(lambda x: x * x, nums)))


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


students = [Student('a', 7), Student('b', 5), Student('c', 3)]
sorted_students = sorted(students, key=lambda x: x.age)
for student in sorted_students:
    print(f"name:{student.name}, age:{student.age}")
