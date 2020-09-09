# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 17:02:54 2020

@author: Garret Bedford
"""

#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Garret Bedford
September 4, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue")
panel.bgpic(image)

#=======Add your code here======
#first, change color and pick up turtle
color(70,102,255)
width(8)
up()
#goto first coordinate
goto(370,-150)
#put down turtle
down()
#goto second coordinate
goto(100,250)
#goto third coordinate
goto(-375,25)
#return to first coordinate
goto(370,-150)
#pick up turtle
up()
#goto first glasses coordinate
goto(-90,115)
#draw the glasses
down()
color('black')
pensize(5)
up()
goto(-100,120)
down()
goto(-30,120)
up()
goto(-15,100)
down()
color("blue")
fillcolor('darkblue')
begin_fill()
circle(16)
end_fill()
color("black")
up()
goto(0,120)
down()
goto(30,120)
up()
goto(40,110)
color("red")
down()
fillcolor('darkred')
begin_fill()
circle(15)
end_fill()
up()
color("black")
goto(58,120)
down()
goto(65,120)