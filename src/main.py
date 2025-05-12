# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       wisdo                                                        #
# 	Created:      4/28/2025, 3:13:11 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

#shared list of list for all screen entities
Screen = []

def newButton(x,y,func):
    x = 0; y= 0; Screen.append([0,x,y,func])# button at 0,0
    # x = 0; y= 0; Screen.append([1,x,y,func])# button at 0,0 #Circular


def warn():
    brain.three_wire_port.a.value(1) 
    # brain.three_wire_port.a.value(0)

# up and down 5 degrees
def angle(dir):
    if dir == 'U':
        pass
    else:
        pass 

# left and right 5 degrees
def turn(dir):
    if dir == 'L' :
        pass
    else:
        pass 

# shooting power
def half():
    pass
def full():
    pass

# self explanitory
def SHOOT():
    pass

# modes 
def weak():
    Screen.clear()
    newButton(0,10,half()) # priming button

    newButton(100,10,turn('L'))
    newButton(100,20,turn('R'))
    newButton(100,30,angle('U'))
    newButton(100,40,angle('D'))
    updateScreen()
    
def strong():
    x = 10; y= 10; Screen.append([0,x,y,full()])# button at 0,0

    x = 100; y= 10; Screen.append([0,x,y,turn('L')])# button at 0,0
    x = 100; y= 20; Screen.append([0,x,y,turn('R')])# button at 0,0
    x = 100; y= 30; Screen.append([0,x,y,angle('U')])# button at 0,0
    x = 100; y= 40; Screen.append([0,x,y,angle('D')])# button at 0,0
    updateScreen()

# initial screen
x = 0; y= 0; Screen.append([0,x,y,weak()])# button at 0,0
x = 10; y= 10; Screen.append([0,x,y,strong()])# button at 0,0

def updateScreen():
    scr= brain.screen 

    scr.set_fill_color(Color(16, 18, 24))
    scr.draw_rectangle(1000,10000,10000,10000) # sets background

  
    brain.screen.set_pen_color(Color.WHITE)
    brain.screen.set_fill_color(Color.BLUE)

    for element in Screen:

        type = element[0]
        x = element[1] 
        y = element[2]

        if type == 0: # buttons
            scr.draw_rectangle(element[1],element[2],5,5)
        if type == 1: # circular buttons
            scr.draw_circle(element[1],element[2],5)
        if type == 3:
            scr.draw_image_from_file('crazy.png',0,0)

def pressed(x,y):
    for element in Screen:
        if x == element[1] and y == element[2]:
            return element[3] # returns the linked function
# pressed callback
brain.screen.pressed(pressed,(brain.screen.x_position,brain.screen.y_position))

# sets up screen
updateScreen()


        
