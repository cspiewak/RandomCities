# Made by: Christopher Spiewak
# Made on: 09-SEP-2019
# Make a 8-bit greyscale 1081×1081 pixel image (PNG) to be used as a heightmap in City Skylines

import random
from PIL import Image, ImageDraw

def is_grey(img, testX, testY, i):
    rgbVal = img.getpixel((testX, testY))
    # make a case switch for all three drawings indicated by the i value
    # use something better than i
    # in each case test the color of pixel to see if it is a suitable starting area

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

def drawSecond(draw):
    # rgb(32, 32, 32)

def drawThird(draw):
    # rgb(64, 64, 64)

def main():
    img = Image.new('RGB', (1081, 1081)) # About 16 pixels per km of map
    draw = ImageDraw.Draw(img)
    drawFirst(draw)
    img.save('generated_map.png') # Every itteration overwrites the last map

if __name__ == "__main__":
    main()
