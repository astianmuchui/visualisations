import turtle

a=0

b=0
#set background
turtle.bgcolor("black")
#set speed
turtle.speed(0)
#set pen color
turtle.pencolor("red")

turtle.goto(0,200)

turtle.pendown()

while True:

   turtle.forward(a)

   turtle.right(b)

   a+=6

   b+=2