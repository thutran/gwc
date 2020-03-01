#
# Author: Jennifer Gomez
#
# This program will draw a regular polygon using turtle graphics. Each of the
# sides will have the same length and each angle will be the same size. The
# number of sides will be chosen by the user (must be greater than 2).


# Import the turtle module
from turtle import *

# Create a function to pick the colors for the fill and border.
def colorPicker(number):
    colors = ['coral', 'gold', 'brown', 'red', 'green', 'blue', 'yellow',
          'purple', 'orange', 'cyan', 'pink', 'magenta', 'goldenrod']
    return colors[number]

# The makePolygon function draws a polygon with the number of sides, side length
# border color, border width, and fill color as specified by the user.
def makePolygon(sides, length, borderColor, width, fillColor):
    s = sides
    begin_fill()
    while s > 0:
        forward(length)
        left(360 / sides)
        s = s - 1
    end_fill()  

# Run the main program
print('This program will draw a polygon with 3 or more sides')
shape('turtle')
showturtle()

# Color of border
import random
number = random.randint(1, 12)
borderColor = pencolor(colorPicker(number))

# Fill color
import random
number = random.randint(1, 12)
fillColor = fillcolor(colorPicker(number))

# Number of Sides
sides = int(input('Enter the number of sides, less than 3 to exit: '))
width = width(sides%20 + 1)
length = 600 / sides
while sides >= 3:
    makePolygon(sides, length, borderColor, width, fillColor)
    sides = int(input('Enter the number of sides, less than 3 to exit: '))
    clear()
    towards(0,0)
