# Sample Code for Python Final Project
# Christopher Lai, Spring 2022
# BWSI RACECAR: Yes, You Can Program Autonomous Cars! Course

class Racecar:
    
    # default constructor
    def __init__(self):
        self.speed = False              # Boolean
        self.color_detect = "black"     # String
        self.orientation = 0            # Int
        self.name = ""

    # user input constructor
    def __init__(self, name):
        self.speed = False              # Default Value
        self.color_detect = "black"     # Default Value
        self.orientation = 0            # Default Value
        self.name = name                # Depends on User Input

    # method to calculate orientation and speed w/ parameter color
    def setRCVector(self, color):
        self.color_detect = color
        # A racecar reaches a junction and has four things to do
        if color == "orange" or color == "purple":
            # turn left
            self.speed = True
            self.orientation = -90
        elif color == "yellow" or color == "brown":
            # turn right
            self.speed = True
            self.orientation = 90
        elif color == "green" or color == "blue":
            # go straight
            self.speed = True
            self.orientation = 0
        else:
            # stop moving
            self.speed = False
            self.orientation = 0 # set direction to straight
        
        # TODO >> TQ: Why don't we return anything in this method?

# FUNCTION 
def parseVector(speed, orientation):
    if not speed:
        return "Not Moving"
    elif speed and orientation == -90:
        return "Turning Left"
    elif speed and orientation == 90:
        return "Turning Right"
    elif speed and orientation == 0:
        return "Going Straight"

def main():
    # create a racecar to start moving it around the junctions we create
    print("Welcome to Chris's Garage!")
    name = input("Please enter the name of your racecar: ")
    racecar1 = Racecar(name)

    # create a dictionary called "database" to keep track of # of junctions
    database = {}

    # create a counter variable to track junctions passed
    counter = 0

    # start the racecar!
    racecar1.speed = True

    # while loop to allow user to input multiple colors
    while racecar1.speed != False:  # Termination Condition
        color = input(f"{racecar1.name} has reached a junction. What is it's color?: ")
        racecar1.setRCVector(color) # change racecar vector depending on color
        
        # create empty dictionary inside while loop to write down junction info
        junction_info = {}
        
        # insert junction info into temp dictionary
        junction_info["name"] = racecar1.name
        junction_info["color_detect"] = racecar1.color_detect
        junction_info["speed"] = racecar1.speed
        junction_info["orientation"] = racecar1.orientation

        # append junction info to database dictionary
        database[counter] = junction_info
        counter += 1

    # generate a neat report summary in the report terminal when racecar has stopped
    print(f"\nThe racecar {racecar1.name} has stopped its journey. Here are the results of its travels!\n")

    # see contents of database dictionary (for testing purposes only)
    # print(database)

    for key in database:
        print(f"Junction #{key + 1}:")
        print(">> Color Detected:", database[key]["color_detect"])
        print(">> Speed:", database[key]["speed"])
        print(">> Orientation:", database[key]["orientation"])
        print(">> Action:", parseVector(database[key]["speed"], database[key]["orientation"]), end="\n\n")

    print("-----End of Journey-----\n")

if __name__ == "__main__":
    main()
