import turtle


def spider(n=12):
    multiple = 50
    turtle.shape("turtle")
    for i in range(1, n + 1):
        turtle.right(360 / n)
        turtle.forward(multiple)
        turtle.stamp()
        turtle.backward(multiple)


if __name__ == "__main__":
    spider()
    while True:
        pass
