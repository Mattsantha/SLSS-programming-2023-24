# Images and Python
# Author: Ubial
# 11 December 2023

from PIL import Image

#Recall that we ca open up fuiles inb Python
with Image.open("./Images/kid-green.jpg") as im:
    # get pixel information from the top left most pixel
    pixel = im.getpixel((0, 0))

    # print the pixel information
    print(pixel)

# Get the middle pixel
middle = im.width 