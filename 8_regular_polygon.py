import turtle


def regular_polygon(n):
    turtle.shape("turtle")
    turtle.pendown()
    turtle.left(90 + 180 / n)
    for i in range(n):
        turtle.forward((n - 1) * 5)
        turtle.left(360 / n)
    turtle.right(90 + 180 / n)
    turtle.penup()
    turtle.forward(10)


if __name__ == "__main__":
    for i in range(3, 13):
        regular_polygon(i)
    while True:
        pass
