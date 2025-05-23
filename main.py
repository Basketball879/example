import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("deepskyblue2")

t=turtle.Turtle()
t.speed(0)

#beach
t.penup()
t.goto(-5000,-100)
t.pendown()
t.fillcolor("bisque2")
t.begin_fill()
t.goto(5000,-100)
t.goto(5000,-5000)
t.goto(-5000,-5000)
t.goto(-5000,-100 )
t.end_fill()
#water
t.penup()
t.goto(-5000,0)
t.pendown()
t.fillcolor("darkblue")
t.begin_fill()
t.goto(5000,0)
t.goto(5000,-150)
t.goto(-5000,-150)
t.goto(-5000,0)
t.end_fill()

# sun
t.pencolor('gold')
t.penup()
t.goto(-250,250)
t.pendown()
t.fillcolor('gold')
t.begin_fill()
t.circle(60)
t.end_fill()

# clouds
t.pencolor('white')
t.penup()
t.goto(150,180)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(50)
t.end_fill()
t.pencolor('white')
t.penup()
t.goto(100,180)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(50)
t.end_fill()
t.pencolor('white')
t.penup()
t.goto(125,205)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(50)
t.end_fill()
t.pencolor('white')
t.penup()
t.goto(150,190)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(50)
t.end_fill()
t.pencolor('white')
t.penup()
t.goto(100,190)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(50)
t.end_fill()



#towel
for i in range(5):
    if i %2==0:
        t.pencolor("blue")
        t.fillcolor("blue")
    else:
        t.pencolor("white")
        t.fillcolor("white")
    t.penup()
    t.goto(-250+i*15,-275)
    t.pendown()
    t.setheading(0)

    t.begin_fill()
    t.forward(15)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(100)
    t.end_fill()

# t.penup()
# t.goto(-250,-275)
# t.pendown()
# t.pencolor("white")
# t.fillcolor("white")
# t.begin_fill()
# t.forward(15)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(15)
# t.left(90)
# t.forward(100)
# t.end_fill()

# t.penup()
# t.goto(-265,-275)
# t.pendown()
# t.pencolor("blue")
# t.fillcolor("blue")
# t.begin_fill()
# t.forward(15)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(15)
# t.left(90)
# t.forward(100)
# t.end_fill()

t.penup()
t.goto(-125,-275)
t.pendown()
t.fillcolor('red')
t.begin_fill()
t.circle(25,180)
t.end_fill()
t.fillcolor('green')
t.begin_fill()
t.circle(25,180)
t.end_fill()

t.penup()

t.goto(-175,150)
t.pendown()

t.pensize(4)
t.left(25)
t.forward(20)

t.left(125)
t.forward(20)



t.penup()

t.goto(-200,150)
t.pendown()

t.pensize(4)
t.left(25)
t.forward(20)

t.left(125)
t.forward(20)




t.penup()

t.goto(-150,150)
t.pendown()

t.pensize(4)
t.left(25)
t.forward(20)

t.left(125)
t.forward(20)

t.penup()
t.goto(100,-50)
t.fillcolor("grey")
t.begin_fill()
t.pendown()
t.goto(150,-50)
t.goto(100,0)
t.goto(100,-50)
t.end_fill()

t.penup()
t.goto(-40,175)
t.pendown()
t.write("SPRING", font=("arial", 30, "bold"), align="center")

#boat
t.penup()
t.goto(-100,50)
t.pendown()
t.color("green")
t.begin_fill()
t.forward(200)
t.right(90)
t.forward(50)
t.right(90)
t.forward(200)
t.end_fill()










t.penup()
turtle.done()