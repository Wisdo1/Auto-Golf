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


def button1():
    # gurt: Yo
    pass
x = 0; y= 0; Screen.append([0,x,y,button1()])# button at 0,0


def updateScreen():
    scr= brain.screen
    scr.set_fill_color(Color.BLUE)

    for element in Screen:

        type = element[0]
        x = element[1] 
        y = element[2]

        if type == 0: # buttons
            scr.draw_rectangle(element[1],element[2],5,5)
        if type == 1: # circular buttons
            scr.draw_circle(element[1],element[2],5)


def pressed(x,y):
    # brain.screen.x_position()
    for element in Screen:
        if x == element[1] and y == element[2]:
            return element[3] # returns the linked function
# pressed callback
brain.screen.pressed(pressed,(brain.screen.x_position,brain.screen.y_position))


updateScreen()



        
