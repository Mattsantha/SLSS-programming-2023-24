# Function turtle
# Author: Matt
# Date: Nov 28 2023

import turtle

burt = turtle.Turtle()

burt.color("lightblue")

def squared(num: float) -> float:
    """Takes a number and squares and returns it."""

    return num ** 2

def draw_square(side_length: int) -> None:
    """Draw a square of a given length."""
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)

    #burt.speed(0)

# Draw squares that groe exponentially
#for i in range(40):
   # draw_square(squared(i))

def draw_tree(level: int, height: int) -> None:
    """A recursive function that draws a tree with initial given height in pixels
    
    Parmas:
    
    level - number representing the levels of branches
    height - height of the main trunk in pixels
    """

    if level > 0:
        # 1. Move turtle forward height pixels
        burt.forward(height)

        # 2. Turn turtle left
        burt.left(36)
        #    a. Draw a smaller tree (current level - 1)
        draw_tree(level - 1, height * 0.75)

        # 3. Turn turtle right
        burt.right(36 * 2)
        #    a. Draw a smaller tree (current level - 1)
        draw_tree(level - 1, height * 0.75)

        # 4. Return to beginning
        burt.left(36)
        burt.back(height)
    else:
        original_colour = burt.color()
        burt.color("green")
        burt.stamp()
        burt.color(original_colour[0]) # revert burt's color

# Set-up Burt to draw trees

def draw_fancy_tree(level: int, height: int) -> None:
    """A recursive function that draws a tree with initial given height in pixels
    
    Parmas:
    
    level - number representing the levels of branches
    height - height of the main trunk in pixels
    """

    if level > 0:
        # 1. Move turtle forward height pixels
        burt.forward(height)

        # 2. Turn turtle left
        burt.left(36)
        #    a. Draw a smaller tree (current level - 1)
        draw_fancy_tree(level - 1, height * .75)

        burt.right(40)
        #    a. Draw a smaller tree (current level - 1)
        draw_fancy_tree(level - 1, height * .75)

        # 3. Turn turtle right
        burt.right(45)
        #    a. Draw a smaller tree (current level - 1)
        draw_fancy_tree(level - 1, height * .9)

        # 4. Return to beginning
        burt.left(49)
        burt.back(height)
    else:
        original_colour = burt.color()
        burt.color("green")
        burt.stamp()
        burt.color(original_colour[0]) # revert burt's color

burt.color("brown")
burt.setheading(90)     # Points Burt north
burt.width(4)           # Trunck and branches thinker
burt.speed(0)

draw_fancy_tree(3, 150)
turtle.done()