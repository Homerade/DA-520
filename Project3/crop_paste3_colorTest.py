import random
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from math import floor

im = Image.open("im_scotch.jpg")
px = im.load()

y1 = im.height/9
y2 = 200

rInt = random.randint(5,20)



for x in range(0,im.width):
    for y in range(0,im.height):
        
        R = px[ x, y ][0]
        G = px[ x, y ][1]
        B = px[ x, y ][2]

        R = B
        G = G-80
        B = B/3

        px[x,y] = ( R, B, G )
               

im.show()