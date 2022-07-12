import turtle

flag = turtle.Turtle()

flag.speed(5)
flag.pensize(5)
flag.color('#000080')
 
# def draw(x, y):
#      flag.penup()
#      flag.goto(x,y)
#      flag.pendown()

#      for i in range(24):
#          flag.forward(80)
#          flag.backward(80)
#          flag.left(15)
#      #flag.backward(80)
#      #draw(0, -80)
#      flag.goto(-100,20)
#      flag.circle(80, 360)    
#      flag.goto(-460,20)
#      flag.begin_fill()
#      flag.color('#138808')
#      flag.forward(720)
#      flag.right(90)
#      flag.forward(160)
#      flag.right(90)
#      flag.forward(720)
#      flag.right(90)
#      flag.forward(160)
#      flag.end_fill()
#      flag.color('#FFFFFF')
#      flag.goto(-460,180)
#      flag.color('#FF9933')
#      #draw(-350,80)

#      flag.begin_fill()
#      flag.color('#FF9933')
#      flag.right(90)
#      flag.forward(720)
#      flag.left(90)
#      flag.forward(160)
#      flag.left(90)
#      flag.forward(720)
#      flag.left(90)
#      flag.forward(160)

#      flag.end_fill()

#      turtle.done()

def draw_circle(x,y,color,radius):
     flag.penup()
     flag.goto(x,y)
     flag.pendown()
     flag.color(color)
     for i in range(24):
         flag.forward(radius)
         flag.backward(radius)
         flag.left(15)
     #flag.backward(80)
     #draw(0, -80)
     flag.goto(-100,20)
     flag.circle(radius, 360) 
     flag.end_fill()  


def draw_rectangle(x,y,color,length,breadth):
     flag.goto(x,y)
     flag.begin_fill()
     flag.color(color)
     flag.forward(length)
     flag.right(90)
     flag.forward(breadth)
     flag.right(90)
     flag.forward(length)
     flag.right(90)
     flag.forward(breadth)
     flag.end_fill()

# def main():
#     print("Hello World!")

if __name__ == "__main__":
    # main() 
    #draw(-100,100)
    draw_circle(-100,100,"#000080",80)
    draw_rectangle(-460,20,"#138808",720,160)
    flag.right(90)
    draw_rectangle(-460,340,"#FF9933",720,160)
    turtle.done()










                





