import turtle

t = turtle.Turtle()

turtle.bgcolor("lightblue")

t.color("red")
t.begin_fill()

for i in range(3):
    t.forward(100)
    t.left(120)

t.end_fill()

t.penup()
t.goto(150, 0)
t.pendown()

t.color("green")
t.begin_fill()

for i in range(2):
    t.forward(120)
    t.left(90)
    t.forward(60)
    t.left(90)

t.end_fill()

t.penup()
t.goto(-150, 0)
t.pendown()

t.color("orange")
t.begin_fill()

for i in range(6):
    t.forward(80)
    t.left(60)

t.end_fill()


turtle.done()