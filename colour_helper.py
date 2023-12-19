# Colour Helper
# Author: Matt
# Dec 13 2023

# Do you need help with colours?
# This is for you!!

def pixel_to_string(pixel: tuple) -> str:
    """Take  rgb 3 tuple and "interperite it" as a colour and return that colour's name
    
    Params: 
        pixel - 3-tuple of (red, green, blue)

    Return:
        string representing the colour
    """

    r,g,b = pixel

    if g > 105 and r < 105 and b < 105:
        return "green"

def is_light(pixel: tuple) -> bool:
    """Returns true if given pixel is "light"

    Params:
        pixel - 3-tuple of values red, green, blue

    Returns:
        True if pixel is light false if not
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    average = (red + green + blue) / 3

    if average >= 128:
        return True
    else:
        return False

black=(0,0,0)
dark_gray=(127,127,127)
light_gray=(128,128,128)
white=(255,255,255)

print(is_light(black)) # False
print(is_light(dark_gray)) # False
print(is_light(light_gray)) # True
print(is_light(white)) # True