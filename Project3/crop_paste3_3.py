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

        ColorsOptions = [
			[R/3, G-80, R],	#green
			[R-80, R, B/3],	#grey
			[B, G-80, B/3],	#orange
			[R/3, -80, G],	#winter
			[R/3, R, B-80],	#deep blue
			[R-80, G/3, G],	#red
			]

	ColorShade = random.choice(ColorsOptions)

	R = R/3
	G = G-80
	B = R

	px[x,y] = (ColorShade)


for y in range(0, im.height, im.height/9):  #im.height/rInt: 'rInt = random.randint(7,20)' random line thicknesses

	rIntX = random.randint(-(im.height-(im.height/9)),im.width)
	rIntY = random.randint(0,im.height)

	y = y + im.height/9
	y2 = y2 + im.height/9

	Section = im.crop(( 0, y, im.width, y2))

	im.paste(Section, (rIntX, rIntY))
               

im.show()