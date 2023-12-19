# Pizza Ubial
# Author: Matt 
# Dec 19 2023

import colour_helper

from PIL import Image

with Image.open("./Images/best_pizza.jpg") as im:
    image_height = im.height
    image_width = im.width

    for y in range(image_height): 
        for x in range(image_width):
            pixel = im.getpixel((x, y))
            if colour_helper.is_light(pixel):
                im.putpixel((x, y), (255, 255, 255))

            else:
                im.putpixel((x, y), (0, 0, 0))

im.save("./Images/output.jpg")
            