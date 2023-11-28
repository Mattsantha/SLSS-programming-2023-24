# Function Practice
# Author: Matt
# Date: November 24 2023

def area_of_a_square(sidelength: float) -> float:
    """Return the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square
    """

    area = sidelength**2

    return area



	
def print_area_of_a_square(sidelength: float):
	"""Calculate and print the area of a sqaure.
	Results are in units squared
	
	Params:
	
	sidelength - length of one side of the square
	"""
	area = sidelength ** 2 
	
	print(f"The area of a square with side length {sidelength} is: {area} square units"
       )

print(print_area_of_a_square(12.2))
# print_area_of_a_square(12)

# Given two squares of two sidelengths
#    12.2 and 144
# Add the area of both squares

# area_of_squares = area_of_a_square(12.2) + area_of_a_square(144)
# print(area_of_squares)

# Question 1
def stars(num_stars: int) -> str:
      """Returns a number of stars
      
      Params:
      
      num_starts - the number of starts to return
      """

      return "*" * num_stars

print(stars(100))

# Queston 2
def biggest_of_three(num_one: float, num_two: float, num_three: float) -> float:
    """Returns the biggest number out of the three
    
    Params:
     
    num_one - first number
    num_two - second number
    num_three - third number
    """

    if num_one > num_two and num_one > num_three:
        return num_one
    if num_two > num_one and num_two > num_three:
           return num_two
    if num_three > num_one and num_three > num_two:
       return num_three
      


print(biggest_of_three(1, 200, 100))

# Question 3
def pyramid(num_layers: int) -> None:
    """Prints out a pyramid of given number of layers.

    Params:

    num_layers - number of layers in the pyramid
    """

    for current_layer in range(1, num_layers + 1):
        print(stars(current_layer))


pyramid(5)
pyramid(10)
pyramid(20)


# Question 4
def pyramid_mirror(num_layers: int) -> None:
    """Prints out a mirrored pyramid.

    Params:
    num_layers - number of layers of pyramid
    """

    for current_layer in range(1, num_layers + 1):
        # Print the spaces then print the stars
        # num_layers == 2
        # " " * 1  +  stars(1)
        # " " * 0   + stars(2)
        # num_layers == 3
        # " " * 2  + stars(1)
        # " " * 1  + stars(2)
        # " " * 0  + stars(3)
        print(" " * (num_layers - current_layer) + stars(current_layer))

pyramid_mirror(20)
pyramid_mirror(30)
pyramid_mirror(14)