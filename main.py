# Made by: Christopher Spiewak
# Made on: 09-SEP-2019
# Make a 8-bit greyscale 1081×1081 pixel image (PNG) to be used as a heightmap in City Skylines

import random
from PIL import Image, ImageDraw, ImageFilter

def drawFirst(draw):
    # Randomly generate the sizes
    n = random.randint(6, 12)
    i = 1
    while i <= n:
        x0 = random.randint(130, 580) # Starting point in the X direction defining the bounding box
        y0 = random.randint(130, 580) # Starting point in the Y direction defining the bounding box
        startCord = (x0, y0)
        x1 = x0 + random.randint(255, 345) # X length
        y1 = y0 + random.randint(255, 345) # Y length
        endCord = (x1, y1)
        draw.ellipse((startCord, endCord), fill='rgb(32, 32, 32)')
        i += 1

def drawSecond(draw):
    # rgb(32, 32, 32)
    n = random.randint(6, 12)
    i = 1
    while i <= n:
        x0 = random.randint(140, 560) # Starting point in the X direction defining the bounding box
        y0 = random.randint(140, 560) # Starting point in the Y direction defining the bounding box
        startCord = (x0, y0)
        x1 = x0 + random.randint(200, 300) # X length
        y1 = y0 + random.randint(200, 300) # Y length
        endCord = (x1, y1)
        draw.ellipse((startCord, endCord), fill='rgb(64, 64, 64)')
        i += 1

def drawThird(draw):
    # rgb(64, 64, 64)
    n = random.randint(6, 12)
    i = 1
    while i <= n:
        x0 = random.randint(180, 520) # Starting point in the X direction defining the bounding box
        y0 = random.randint(180, 520) # Starting point in the Y direction defining the bounding box
        startCord = (x0, y0)
        x1 = x0 + random.randint(100, 200) # X length
        y1 = y0 + random.randint(100, 200) # Y length
        endCord = (x1, y1)
        draw.ellipse((startCord, endCord), fill='rgb(128, 128, 128)')
        i += 1

def main():
    img = Image.new('RGB', (1081, 1081)) # About 16 pixels per km of map
    draw = ImageDraw.Draw(img)
    # Draw the levels of elevation
    drawFirst(draw)
    drawSecond(draw)
    drawThird(draw)
    img.save('generated_map.png') # Save the map
    # Cut out sharp corners of the topology
    postImg1 = Image.open('generated_map.png')
    simg1 = postImg1.filter(ImageFilter.ModeFilter(size = 20))
    simg1.save('generated_map_post.png')
    # Smooth the topology
    postImg2 = Image.open('generated_map_post.png')
    simg2 = postImg2.filter(ImageFilter.BoxBlur(radius = 50))
    simg2.save('generated_map_post.png')

if __name__ == "__main__":
    main()
