import turtle
from math import sin, cos, pi


def spiral():
    turtle.shape("turtle")
    a = 0
    multiple = 50
    turtle.penup()
    while True:
        a += 1 * pi / 360
        p = a / (2 * pi) * multiple
        turtle.goto(p * cos(a), p * sin(a))
        turtle.pendown()


if __name__ == "__main__":
    spiral()
    while True:
        pass
