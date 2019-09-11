# Made by: Christopher Spiewak
# Made on: 09-SEP-2019
# Make a 8-bit greyscale 1081×1081 pixel image (PNG) to be used as a heightmap in City Skylines

import random
from PIL import Image, ImageDraw

def drawFirst(draw):
    # Draw the lage rectangles/squares of no more than 4km by 4km in size (Max: 420px lol Min: 210px)
    # Randomly generate the sizes
    i = 1
    while i <= 6:
        x0 = random.randint(100, 981)
        y0 = random.randint(100, 981)
        startCord = (x0, y0)
        x1 = x0 + random.randint(210, 400) # X length
        y1 = y0 + random.randint(210, 400) # Y length
        endCord = (x1, y1)
        draw.rectangle((startCord, endCord), fill='hsl(240, 0%, 6.25%)') # (black=0%, normal=50%, white=100%)
        i += 1

def main():
    img = Image.new('RGB', (1081, 1081)) # About 60 pixels per km of map
    draw = ImageDraw.Draw(img)
    drawFirst(draw)
    img.save('generated_map.png') # Every itteration overwrites the last map

if __name__ == "__main__":
    main()
