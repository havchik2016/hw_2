import turtle


def rect_spiral():
    turtle.shape("turtle")
    c = 1
    while True:
        turtle.forward(c * 10)
        turtle.left(90)
        c += 1


if __name__ == "__main__":
    rect_spiral()
    while True:
        pass
