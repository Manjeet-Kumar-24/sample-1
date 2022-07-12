import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(5)
t=tommy

# def draw_rectangle(turtle, color, length, breadth, x, y):
#     turtle.penup()
#     turtle.color(color)
#     turtle.fillcolor(color)
#     turtle.goto(x,y)
#     turtle.begin_fill()
#     turtle.forward(length) # Forward turtle by s units
#     turtle.left(90) # Turn turtle by 90 degree
     
#     # drawing second side
#     turtle.forward(breadth) # Forward turtle by s units
#     turtle.left(90) # Turn turtle by 90 degree
     
#     # drawing third side
#     turtle.forward(length) # Forward turtle by s units
#     turtle.left(90) # Turn turtle by 90 degree
     
#     # drawing fourth side
#     turtle.forward(breadth) # Forward turtle by s units
#     turtle.left(90) # Turn turtle by 90 degree
#     turtle.end_fill()
#     turtle.pendown()


def draw_left_rectangle(x,y,length,breadth,length2,angle,colour):
  t.penup()
  t.goto(x,y)
  t.color(colour)
  t.fillcolor(colour)
  t.begin_fill()
  t.pendown()
  t.left(21)
  t.forward(breadth)
  t.left(69)
  t.forward(length2)
  t.left(69)
  t.forward(breadth)
  t.left(111)
  t.forward(length)
  t.end_fill()
  t.pendown()

def draw_right_rectangle(x,y,length,breadth,length2,angle,colour):
  t.penup()
  t.goto(x,y)
  t.color(colour)
  t.fillcolor(colour)
  t.begin_fill()
  t.pendown()
  t.left(21)
  t.forward(breadth)
  t.left(69)
  t.forward(length2)
  t.left(69)
  t.forward(breadth)
  t.left(111)
  t.forward(length)
  t.end_fill()
  t.pendown()
  
  
draw_circle(tommy, "#FF3300", 45, -100, 120)

draw_left_rectangle(-200,-200,283.46,98.4,245.66,21,"#FF3300")
t.left(90)

draw_left_rectangle(-232,-200,290.46,31,288.66,21,"#FF6600")
t.left(90)

draw_left_rectangle(-264,-200,290.46,31,288.66,21,"#FF9900")
t.left(90)

draw_left_rectangle(-296,-200,290.46,31,288.66,21,"#FFCC00")
t.right(90)

draw_right_rectangle(-10,115,283.46,98.4,245.66,21,"#FF3300")
t.left(90)

draw_right_rectangle(22,112,290.46,31,288.66,21,"#FF6600")
t.left(90)

draw_right_rectangle(54,112,290.46,31,288.66,21,"#FF9900")
t.left(90)

draw_right_rectangle(86,112,290.46,31,288.66,21,"#FFCC00")
t.right(90)

t.hideturtle()
turtle.done()