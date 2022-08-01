"""
Copyright MIT and Harvey Mudd College
MIT License
Summer 2020

Lab 1 - Driving in Shapes
"""

# Imports
########################################################################################

import sys

sys.path.insert(1, "../../library")
import racecar_core
import racecar_utils as rc_utils

########################################################################################
# Global variables
#######################################################################################

rc = racecar_core.create_racecar()

counter = 0
isDriving = False 
square = False

########################################################################################
# Functions
########################################################################################


def start():
  rc.drive.stop()
  print("The car has started.")

  print(
       """>> Lab 1 - Driving in Shapes\n"
        "\n"
        "Controls:\n"
        "Right trigger = accelerate forward\n"
        "Left trigger = accelerate backward\n"
        "Left joystick = turn front wheels\n"
        " A button = drive in a circle\n"
        11" B button = drive in a square\n"
        "X button = drive in a figure eight\n"""
  )

    # TODO (main challenge): add a line explaining what the Y button does

def update():
    global counter
    global isDriving
    global square
    
    # TODO (warmup): Implement acceleration and steering

    # TODO (main challenge): Drive in a circle

    if rc.controller.was_pressed(rc.controller.Button.A):
        print("Driving in a circle...")
        isDriving = True
        counter = 0
        if isDriving:
            counter += rc.get_delta_time()
        elif counter < 6:
            rc.drive.set_speed_angle(1,1)
        else:
            rc.drive.stop()

    # TODO (main challenge): Drive in a square when the B button is pressed

    if rc.controller.was_pressed(rc.controller.Button.B):
        print("Driving in a square...")
        counter = 0
        square = True

    if square: 
        counter += rc.get_delta_time()

        if counter < 1:
            rc.drive.set_speed_angle(1,0)
        elif counter < 2:
            rc.drive.set_speed_angle(1,1)
        elif counter < 3: 
            rc.drive.set_speed_angle(1,1)
        elif counter < 4:
            rc.drive.speed_angle(1,0)
        else:
            rc.drive.stop()
            square = False 


    # TODO (main challenge): Drive in a figure eight when the X button is pressed

    # TODO (main challenge): Drive in a shape of your choice when the Y button
    # is pressed
"""

########################################################################################
# DO NOT MODIFY: Register start and update and begin execution
########################################################################################
"""
if __name__ == "__main__":
    rc.set_start_update(start, update)
    rc.go()
