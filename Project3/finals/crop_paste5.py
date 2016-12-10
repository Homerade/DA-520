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

        R = R/3
        G = G-80
        B = G

        px[x,y] = ( R, B, G )



for y in range(0, im.height, im.height/rInt):  #im.height/rInt: 'rInt = random.randint(7,20)' random line thicknesses

	rIntX = random.randint(-(im.height-(im.height/9)),im.width)
	rIntY = random.randint(0,im.height)

	y = y + im.height/9
	y2 = y2 + im.height/9

	Section = im.crop(( 0, y, im.width, y2))

	im.paste(Section, (rIntX, rIntY))
               

im.show()