import turtle


def circle():
    turtle.shape("turtle")
    for i in range(360):
        turtle.left(1)
        turtle.forward(1)


if __name__ == "__main__":
    circle()
    while True:
        pass
