from PIL import Image, ImageFilter
from math import hypot, pi, cos, sin


image = Image.open('scrabble-board.jpg')

houghed = hough(image)
img.save('output.png')

#pixel values to crop
cords = (100,100,400,400)

cropped  = img.crop(cords)

cropped.show()
