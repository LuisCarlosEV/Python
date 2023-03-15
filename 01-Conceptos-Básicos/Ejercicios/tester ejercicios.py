import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.bgcolor("green")
t.shape("turtle")
t.pencolor()
t.fillcolor()
t.pensize(5)

t.begin_fill()
t.fd(100)
t.rt(90)
t.fd(100)
t.end_fill()

t.circle(60)

turtle.exitonclick()