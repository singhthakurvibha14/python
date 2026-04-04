import turtle

t = turtle.Turtle()
t.speed(3)

# function to draw filled square
def square(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

# front face
square(-50, -50, "light green")

# top face
t.penup()
t.goto(-50, 50)
t.pendown()
t.fillcolor("light blue")
t.begin_fill()
t.goto(0, 100)
t.goto(100, 100)
t.goto(50, 50)
t.goto(-50, 50)
t.end_fill()

# side face
t.penup()
t.goto(50, -50)
t.pendown()
t.fillcolor("pink")
t.begin_fill()
t.goto(100, 0)
t.goto(100, 100)
t.goto(50, 50)
t.goto(50, -50)
t.end_fill()

turtle.done()