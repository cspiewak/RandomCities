# Made by: Christopher Spiewak
# Made on: 09-SEP-2019
# Make a 8-bit greyscale 1081×1081 pixel image (PNG) to be used as a heightmap in City Skylines

import random
import colorsys # Used to find the area of the previous obj generation
from PIL import Image, ImageDraw

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
        draw.ellipse((startCord, endCord), fill='hsl(240, 0%, 6.25%)') # (black=0%, normal=50%, white=100%)
        i += 1

def main():
    img = Image.new('RGB', (1081, 1081)) # About 16 pixels per km of map
    draw = ImageDraw.Draw(img)
    drawFirst(draw)
    img.save('generated_map.png') # Every itteration overwrites the last map

if __name__ == "__main__":
    main()
