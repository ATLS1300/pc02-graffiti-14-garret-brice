#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:55:19 2020

@author: bricewilson
"""
'''
ATLS 1300
Author: Brice Wilson
September 4, 2020
'''

from turtle import * 

colormode(255)


panel = Screen()
w = 750 
h = 750 
panel.setup(width=w, height=h) 



image = "Bezos 2.gif"
panel.bgcolor("lightsteelblue")
panel.bgpic(image)

pensize(5)
up()
goto(-100,120)
down()
goto(-30,120)
up()
goto(-15,100)
down()
color("blue")
fillcolor("darkblue")
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
fillcolor("darkred")
begin_fill()
circle(15)
end_fill()
up()
color("black")
goto(58,120)
down()
goto(65,120)
color(70,102,255)
width(8)
up()
goto(370,-150)
down()
goto(100,250)
goto(-375,25)
goto(370,-150)


