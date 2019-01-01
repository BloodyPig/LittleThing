# 科赫曲线
# 正整数n代表科赫曲线的阶数，表示生成科赫曲线过程的操作次数。
# 科赫曲线初始化阶数为0，表示一个长度为L的直线。
# 对于直线L将其等分为3段，中间一段用边长为L/3的等边三角形的两个边替代，
# 得到1阶科赫曲线，它包含4条线段。进一步对每条线段重复同样的操作后得到的2阶科赫曲线。
# 重复操作N次可以得到N阶科赫曲线。

import turtle
from turtle import *


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)


def main():
    turtle.setup(720, 720)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(1)
    level = 5
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle()
    done()


main()
