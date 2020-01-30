import turtle


def nested_rectangle():
    turtle.shape("turtle")
    for i in range(1, 11):
        turtle.forward(10 * i)
        turtle.left(90)
        turtle.forward(10 * i)
        turtle.left(90)
        turtle.forward(10 * i)
        turtle.left(90)
        turtle.forward(10 * i)
        turtle.penup()
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(5)
        turtle.right(180)
        turtle.pendown()


if __name__ == "__main__":
    nested_rectangle()
    while True:
        pass
