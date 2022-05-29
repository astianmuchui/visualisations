import turtle
x = turtle.Turtle()
x.getscreen().bgcolor("#00030a")
x.pencolor("#2fa4e7")
x.speed(10)
x.penup()
x.goto(-250,100)
x.pendown()
def star_recur(turtle,y):
    if y<=10:
        return
    else:
        for i in range(10):
            turtle.forward(y)
            star_recur(turtle,y/3)
            turtle.left(216)
star_recur(x,360)
turtle.done()
