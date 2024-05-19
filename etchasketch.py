from turtle import Turtle, Screen

tuktuk = Turtle()
screen = Screen()


def forward():
    tuktuk.forward(10)


def backward():
    tuktuk.backward(10)


def right():
    tuktuk.right(20)


def left():
    tuktuk.left(20)


def clear():
    # tuktuk.clear()
    tuktuk.reset()


screen.listen()

screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
