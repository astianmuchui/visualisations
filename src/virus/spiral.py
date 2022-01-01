import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.width(2)
t.speed(15)

col = ('white','green','black')
for i in range(300):
   t.pencolor(col[1%3])
   t.forward(i*4)
   t.right(121)