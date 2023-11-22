# Turtle Example
# Author: Matt Santha
# Date: November 21 2023

import turtle 

# Create a turtle that can be moved around the screen

FORWARD_MAGNITUDE = 20
LEFT_MAGNITUDE = 20
RIGHT_MAGNITUDE = 20
# Make a turtle object
michaelango = turtle.Turtle()

# Get some input from the user
print("""To give commands, type:
      F - to go forward
      L - to turn left
      R - to turn right.""")

# Repeat the below forever, or until the user syas stop. 
done = False 

while not done:
    command = input("Where should I go?")

    #  Move the turtle around based on that input
    #Stop if the user says stop
    if command.strip(",.?!").lower() == "f":
        michaelango.forward(FORWARD_MAGNITUDE)
    elif command.strip(",.?!").lower() == "l":
        michaelango.left(LEFT_MAGNITUDE)
    elif command.strip(",.?!").lower() == "r":
        michaelango.right(RIGHT_MAGNITUDE)
    elif command == "stop":
        done = True

