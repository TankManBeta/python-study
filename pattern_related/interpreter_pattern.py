# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/2 8:26
"""


class Context:
    def __init__(self):
        self.input = ""
        self.output = ""


class AbstractExpression:
    def Interpret(self, context):
        pass


class Expression(AbstractExpression):
    def Interpret(self, context):
        print("terminal interpret")


class NonterminalExpression(AbstractExpression):
    def Interpret(self, context):
        print("Nonterminal interpret")


if __name__ == "__main__":
    context = ""
    c = []
    c = c + [Expression()]
    c = c + [NonterminalExpression()]
    c = c + [Expression()]
    c = c + [Expression()]
    for a in c:
        a.Interpret(context)
