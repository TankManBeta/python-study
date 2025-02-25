# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/11/25 13:07
"""


class Factory:
    def manufacture(self, brand):
        if brand == "Benz":
            return Benz()
        elif brand == "Ferrari":
            return Ferrari()


class Benz:
    def __init__(self):
        print("I am Benz")


class Ferrari:
    def __init__(self):
        print("I am Ferrari")


if __name__ == "__main__":
    factory = Factory()
    factory.manufacture("Benz")
    factory.manufacture("Ferrari")