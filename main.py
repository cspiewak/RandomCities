# Made by: Christopher Spiewak
# Made on: 09-SEP-2019
# Make a 8-bit greyscale 1081×1081 pixel image (PNG) to be used as a heightmap in City Skylines

from os.path import dirname, abspath
from PIL import Image, ImageDraw

def drawFirst():
    ImageDraw.ImageDraw.rectangle()

def main():
    PATH_NAME = dirname(dirname(abspath(__file__)))

    img = Image.new('L', (1081, 1081)) # About 60 pixels per km of map
    img.save('generated_map.png') # Every itteration overwrites the last map

if __name__ == "__main__":
    main()
