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

buzz = DigitalOut(brain.three_wire_port.a)

turntable = Motor(1,False)
pivot = Motor(2,False)


#shared list of list for all screen entities
SCREENSTR = []

def updateScreen():
    scr= brain.screen 

    scr.draw_rectangle(0,0,10000,10000,Color(16, 18, 24)) # sets background

  
    brain.screen.set_pen_color(Color.WHITE)
    brain.screen.set_fill_color(Color.BLUE)

    for element in SCREENSTR:

        type = element[0]
        x = element[1] 
        y = element[2]

        if type == 0: # buttons
            scr.draw_rectangle(element[1],element[2],5,5)
        if type == 1: # circular buttons
            scr.draw_circle(element[1],element[2],5)
        if type == 2:
            scr.draw_image_from_file('crazy.png',0,0)


def warn():
    buzz.set(True)
def unwarn():
    buzz.set(False)


# up and down 5 degrees
def angle(dir):
    if dir == 'U':
        # pivot.set_position(turntable.position()+5)
        pass
    else:
        # pivot.set_position(turntable.position()-5) 
        pass

# left and right 5 degrees
def turn(dir):
    if dir == 'L' :
        # turntable.set_position(turntable.position()+5)
        pass
    else:
        # turntable.set_position(turntable.position()-5) 
        pass

# shooting power
def half():
    pass
def full():
    pass

# self explanitory
def SHOOT():
    warn()

def reset():
    # initial screen
    x = 0
    y= 0
    SCREENSTR.append((0,x,y,weak()))# button at 0,0
    x = 10; y= 10; SCREENSTR.append([0,x,y,strong()])# button at 0,0

# modes 
def weak():
    SCREENSTR.clear() # resets our screen storage
    # newButton(0,10,half()) # priming button

    # newButton(100,10,turn('L'))
    # newButton(100,20,turn('R'))
    # newButton(100,30,angle('U'))
    # newButton(100,40,angle('D'))

    # newButton(100,40,reset())
    updateScreen()
    
def strong():
    x = 10; y= 10; SCREENSTR.append([0,x,y,full()])# button at 0,0

    x = 100; y= 10; SCREENSTR.append([0,x,y,turn('L')])# button at 0,0
    x = 100; y= 20; SCREENSTR.append([0,x,y,turn('R')])# button at 0,0
    x = 100; y= 30; SCREENSTR.append([0,x,y,angle('U')])# button at 0,0
    x = 100; y= 40; SCREENSTR.append([0,x,y,angle('D')])# button at 0,0
    updateScreen()



def pressed(x,y):
    for element in SCREENSTR:
        if x == element[1] and y == element[2]:
            return element[3] # returns the linked function
        
# pressed callback
brain.screen.pressed(pressed,(brain.screen.x_position,brain.screen.y_position))

# sets up screen
reset()
updateScreen()