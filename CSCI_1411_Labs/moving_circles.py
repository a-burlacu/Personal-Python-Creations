"""
Task:
Using the graphics package, create several circle graphics based on user-provided object characteristics then manipulate them on the screen via mouse click. 
Create a program that does the following things:
    1. Ask the user for the name of the graphics window
    2. Ask the user for specifications for circle1 (color, center, radius)
    3. Draw and display circle1
    4. Create a second circle (circle2) with the following properties:
        -Radius 1/2 the radius of the circle1
        -Green color
        -Distance between circle1 and circle2 center is twice the radius of circle1
        -Initiall position of circle2 is 90 degrees above circle1
    5. Draw and display circle2
    6. Draw a red line connecting the centers of the circles
    7. On each mouse click, move circle2 90 deg to the right around circle1
"""
#Make sure graphics.py library is in the same folder as this file when running it
from graphics import *

def moving_circles():
    #Ask user the name for the graphics display window
    win_name = input("What would you like the name of the display window to be?: ")
    
    #Ask user for the color of their circle
    color1 = input("What color would you like the circle to be (blue, green, red, yellow)?: ")
    
    #Ask user for coordinated of the center of first circle
    x1,y1 = eval(input("What are the x,y coordinates of the center of the circle?: "))

    #Recall** eval() takes a string and interprets it as an expression (returns result as int)
    #Ask user for the radius of first circle
    radius1 = eval(input("What is the radius of this circle?: "))
    
    #Create the window object using the user input name and a default size of 500x500
    win = GraphWin(win_name, 500,500)

    #Create a circle at (x1,y1) with a radius(radius1) and color(color1) specified 
    center1 = Point(x1, y1)
    circle1 = Circle(center1, radius1)
    circle1.setFill(color1)
    circle1.draw(win)

    #Create the second circle using specifications provided
    x2 = x1
    y2 = y1-(2*radius1)
    radius2 = (radius1/2)
    center2 =Point(x2,y2)
    circle2 = Circle(center2,radius2)
    circle2.setFill("green")
    circle2.draw(win)

    #Draw red line connecting circle centers
    line = Line(center1, center2)
    line.setFill("red")
    line.draw(win)

    for i in range(4):
        d = 2*radius1
        win.getMouse()
        line.undraw()
        if i==0:
            circle2.move(d,d)
        elif i==1:
            circle2.move(-d,d)
        elif i==2:
            circle2.move(-d,-d)
        elif i==3:
            circle2.move(d,-d)  
        i += 1 
        line = Line(center1,circle2.getCenter())
        line.setFill("red")
        line.draw(win) 

    win.getMouse()


moving_circles()