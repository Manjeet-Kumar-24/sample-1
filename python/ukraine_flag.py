import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(2)

def draw_rectangle(turtle, color, length, breadth, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.forward(length) # Forward turtle by s units
    turtle.left(90) # Turn turtle by 90 degree
     
    # drawing second side
    turtle.forward(breadth) # Forward turtle by s units
    turtle.left(90) # Turn turtle by 90 degree
     
    # drawing third side
    turtle.forward(length) # Forward turtle by s units
    turtle.left(90) # Turn turtle by 90 degree
     
    # drawing fourth side
    turtle.forward(breadth) # Forward turtle by s units
    turtle.left(90) # Turn turtle by 90 degree
    turtle.end_fill()
    turtle.pendown()
    


draw_rectangle(tommy, "#0057b7", 240, 80, -100, 0)
draw_rectangle(tommy, "#ffd700", 240, 80, -100, -80)
turtle.done()