"""
Task: 
Using the graphics package, create several circle graphics based on user-provided object characteristics(size, shape, color).
"""
#Make sure graphics.py library is in the same folder as this file when running it
from graphics import *

def circle_creator():
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

    #Repeat the process for the second circle
    color2 = input("\nWhat color would you like the next circle to be?: ")
    x2,y2 = eval(input("What are the x,y coordinates of the center of the second circle?: "))
    radius2 = eval(input("What is the radius of the second circle?: "))
    center2 = Point(x2,y2)
    circle2 = Circle(center2, radius2)
    circle2.setFill(color2)
    circle2.draw(win)

    #Now draw a red line connecting the centers of the two circles
    line = Line(center1, center2)
    line.setFill("red")
    line.draw(win)

    win.getMouse() #This will wait for a mouse click from the user before continuing
    
    #Create a loop that will move the circle 10(arbitrary num) points in the x&y directions
    for i in range(10):
        circle1.move(10,10)
        line.undraw() #This will remove the line
        time.sleep(1) #This will tell the computer to pause for 1sec so the user can see the movement
    #Redraw the line connecting the circles
    line = Line(circle1.getCenter(),center2)
    line.setFill("red")
    line.draw(win)
   
circle_creator()