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

motor = Motor(Ports.PORT1)

motor.set_velocity(50)
motor.spin_to_position(180)
wait(300)
motor.spin_to_position(0)
motor.set_velocity(100)
motor.spin_to_position(180)
wait(300)
motor.spin_to_position(0)
motor.set_velocity(200)
motor.spin_to_position(180)
wait(300)
motor.spin_to_position(0)
