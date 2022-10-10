import turtle

t= turtle. Turtle

def hexagon(t,x,y,color,width,sidelen):
    # code to draw the hexagon
    t.penup()
    t.goto(x,y)
    t.color(color)
    t.width(width)
    t.pendown()
    #draw a hexagon
    for i in range (6):
        t.forward (sidelen)
        t.right(60)
 
def ngon(t,numsides,x,y,color,width,sidelen):
    # code to draw a ngon
    t.penup()
    t.goto(x,y)
    t.color(color)
    t.width(width)
    t.pendown()
    myangle = 360/numsides
    # draw a ngon
    for i in range (numsides):
        t.forward(sidelen)
        t.right(myangle)
    
wn = turtle.Screen()

crush = turtle. Turtle()
hexagon(crush,40,40,"blue",6,50)

squirt = turtle. Turtle()
ngon(squirt,12,100,100,"pink",5,50)


wn.exitonclick()
wn.mainloop()