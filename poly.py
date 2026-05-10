import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

t = turtle.Turtle()
t.pensize(3)
t.speed(3)

def draw_polygon(sides, length):
    angle = 360 / sides
    t.begin_fill()
    for _ in range(sides):
        t.forward(length)
        t.right(angle)
    t.end_fill()

t.penup()
t.goto(-200, 100)
t.pendown()
draw_polygon(3, 120,)

t.penup()
t.goto(50, 100)
t.pendown()
draw_polygon(6, 70,)

t.penup()
t.goto(-80, -150)
t.pendown()
draw_polygon(4,50)

t.hideturtle()
turtle.done()
