import turtle
turtle.Screen().bgcolor("black")
sc=turtle.Screen()
sc.setup(1000,1000)
pen=turtle.Turtle()
colors=["red","purple","blue","green","orange","yellow"]
pen.speed(0)

for i in range(1000):
    pen.color(colors[i % 6])
    pen.forward(i)
    pen.left(59)

turtle.done()