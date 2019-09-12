# Made by: Christopher Spiewak
# Made on: 09-SEP-2019
# Make a 8-bit greyscale 1081×1081 pixel image (PNG) to be used as a heightmap in City Skylines

import random
import numpy as np
from PIL import Image, ImageDraw

def is_grey(val):
    # In each case test the color of pixel to see if it is a suitable starting area
    imgTest = Image.open('generated_map.png', 'r')
    width, height = imgTest.size
    pixel_values = list(imgTest.getdata())
    pixel_values = np.array(pixel_values).reshape((width, height)) # need to add a way of removing the unwanted values for the following test
    if val == 0: # Test for the second drawing of obj
        # (16, 16, 16):

    else: # Test for the third drawing of obj
        # (32, 32, 32):


def drawFirst(draw):
    # Randomly generate the sizes
    n = random.randint(6, 12)
    i = 1
    while i <= n:
        x0 = random.randint(100, 600) # Starting point in the X direction defining the bounding box
        y0 = random.randint(100, 600) # Starting point in the Y direction defining the bounding box
        startCord = (x0, y0)
        x1 = x0 + random.randint(275, 375) # X length
        y1 = y0 + random.randint(275, 375) # Y length
        endCord = (x1, y1)
        draw.ellipse((startCord, endCord), fill='rgb(16, 16, 16)')
        i += 1

def drawSecond(img, draw):
    # rgb(32, 32, 32)
    n = random.randint(6, 12)
    i = 1
    while i <= n:
        testingVal = 0
        while testingVal == 0:
            x0 = random.randint(120, 580) # Starting point in the X direction defining the bounding box
            y0 = random.randint(120, 580) # Starting point in the Y direction defining the bounding box
            testingVAL = is_grey(img, x0, y0, 0)
        startCord = (x0, y0)
        x1 = x0 + random.randint(295, 355) # X length
        y1 = y0 + random.randint(295, 355) # Y length
        endCord = (x1, y1)
        draw.ellipse((startCord, endCord), fill='rgb(32, 32, 32)')
        i += 1

def drawThird(img, draw):
    # rgb(64, 64, 64)
    n = random.randint(6, 12)
    i = 1
    while i <= n:
        testingVal = 0
        while testingVal == 0:
            x0 = random.randint(140, 560) # Starting point in the X direction defining the bounding box
            y0 = random.randint(140, 560) # Starting point in the Y direction defining the bounding box
            testingVAL = is_grey(img, x0, y0, 1)
        startCord = (x0, y0)
        x1 = x0 + random.randint(315, 335) # X length
        y1 = y0 + random.randint(315, 335) # Y length
        endCord = (x1, y1)
        draw.ellipse((startCord, endCord), fill='rgb(32, 32, 32)')
        i += 1

def main():
    img = Image.new('RGB', (1081, 1081)) # About 16 pixels per km of map
    draw = ImageDraw.Draw(img)
    drawFirst(draw)
    drawSecond(img, draw)
    drawThird(img, draw)
    img.save('generated_map.png') # Every itteration overwrites the last map

if __name__ == "__main__":
    main()
