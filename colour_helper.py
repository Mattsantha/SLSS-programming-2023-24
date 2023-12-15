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