# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/11/7 21:36
"""
# 画奥运五环
import turtle

turtle.width(10)

turtle.color("blue")
turtle.circle(50)

turtle.penup()
turtle.goto(120, 0)
turtle.pendown()

turtle.color("black")
turtle.circle(50)

turtle.penup()
turtle.goto(240, 0)
turtle.pendown()

turtle.color("red")
turtle.circle(50)

turtle.penup()
turtle.goto(60, -50)
turtle.pendown()

turtle.color("yellow")
turtle.circle(50)

turtle.penup()
turtle.goto(180, -50)
turtle.pendown()

turtle.color("green")
turtle.circle(50)

