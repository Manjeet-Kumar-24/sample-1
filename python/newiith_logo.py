import turtle

flag = turtle.Turtle()

flag.speed(3)
flag.pensize(2)
flag.color("blue")



def draw(x, y):
#      flag.penup()
#      flag.goto(x,y)
#      flag.pendown()
     
#      flag.circle(80)

       flag.begin_fill()
       flag.fillcolor("red")
       flag.goto(-100,48.04)
       flag.circle(51.96,360)

       flag.end_fill()
       flag.goto(-100,7.5)
       flag.begin_fill()
       flag.fillcolor("orange")
       flag.right(21)
       flag.backward(94.4)
       flag.right(69)
       flag.forward(283.4)
       flag.left(111)
       flag.forward(94.4)
       flag.left(69)
       flag.forward(213.4)
    
       flag.end_fill()
       flag.goto(-92.45,7.5)
       flag.begin_fill()
       flag.fillcolor("orange")
       flag.right(69)
       flag.forward(94.4)
       flag.right(111)
       flag.forward(283.4)
       flag.right(111)
       flag.forward(94.4)
       flag.right(69)
       flag.forward(213.4)
       flag.right(69)
       flag.end_fill()
       
       flag.begin_fill()
       flag.fillcolor("orange")

       flag.forward(94.4)
       flag.forward(8.5)
       flag.right(111)
       flag.forward(273.4)
       flag.left(69)
       flag.forward(20.5)
       flag.left(111)
       flag.forward(273.4)
       flag.left(111)
       flag.forward(20.5)
       flag.end_fill()

       turtle.done()
if __name__ == "__main__":
    # main() 
    draw(-100, 100)

    
        