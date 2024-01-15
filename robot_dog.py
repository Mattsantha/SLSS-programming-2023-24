# Robot Dog
# Author: Matt
# 11 January 2024

from  PIL import Image

import colour_helper

red_ball_image = Image.open("./Images/Red Ball.jpeg")

red_pixels = []

# Get all the pixels in the image
def middle():
    for y in range(red_ball_image.height):
        for x in range(red_ball_image.width):
         current_pixel = red_ball_image.getpixel((x, y))
         
         if colour_helper.pixel_to_string(current_pixel) == "red":
                red_pixels.append((x, y))

    mid_x = sum(coord[0] for coord in red_pixels) // len(red_pixels)
    mid_y = sum(coord[1] for coord in red_pixels) // len(red_pixels)
    return f'({mid_x}, {mid_y})'

print(middle())

red_ball_image.close()