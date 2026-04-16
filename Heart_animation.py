import turtle
import math
import time

#screen/window setup
window=turtle.Screen()
window.bgcolor("dark grey")
window.title("To Friendship")

t=turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(3)
turtle.tracer(0)

#heart function
def heart_outline(scale,color,delay=0.005):
    t.color(color)
    t.penup()

    for i in range(360):
        x=scale * 16 * math.sin(math.radians(i))**3
        y=scale *(
            13 * math.cos(math.radians(i))
            -5*math.cos(2* math.radians(i))
            - 2* math.cos(3 * math.radians(i))
            - math.cos(4 * math.radians(i))
        )
        if i==0:
            t.goto(x,y)
            t.pendown()
        else:
            t.goto(x,y)
        if i % 10==0:
            turtle.update()

        time.sleep(delay)

def heart_fill(scale, color):
    t.color(color)
    t.begin_fill()

    for i in range(360):
        x = scale * 16 * math.sin(math.radians(i))**3
        y = scale * (
            13 * math.cos(math.radians(i))
            - 5 * math.cos(2 * math.radians(i))
            - 2 * math.cos(3 * math.radians(i))
            - math.cos(4 * math.radians(i))
        )
        t.goto(x, y)

    t.end_fill()


#Draw heart
t.penup()
t.goto(0,-10)
t.pendown()
heart_outline(12,"light grey",delay=0.005)

t.penup()
t.goto(0,-10)
t.pendown()
heart_fill(12,"light grey")

t.penup()
t.goto(0,-10)
t.pendown()
heart_outline(10,"Teal")

t.penup()
t.goto(0,-10)
t.pendown()
heart_fill(10,"Teal")

t.penup()
t.goto(0,-10)
t.pendown()
heart_outline(8,"grey")

t.penup()
t.goto(0,-10)
t.pendown()
heart_fill(8,"grey")

#Write text
t.penup()
t.color("black")
t.goto(0,-170)
t.write("Been Nice Talking To You",font=("Times New Roman",22,"bold italic"),align="center")


turtle.update()
turtle.done()
window.mainloop()
