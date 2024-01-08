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
    return pixel >= (128, 128, 128)

def pixel_to_grayscale(pixel: tuple) -> tuple:
    """Returns a grayscale version of the given pixel"""
    gray = int(pixel[0] * 0.3 + pixel[1] * 0.59 + pixel[2] * 0.11)

    return (gray, gray, gray)