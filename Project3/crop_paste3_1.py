	from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from math import floor

im = Image.open("im_pancake.jpg")
px = im.load()

y1 = im.height/9
y2 = 200


for y in range(0, im.height, im.height/9):

	a = im.width/4
	# a = a*(-1)

	y = y + im.height/9
	y2 = y2 + im.height/9

	Section = im.crop(( 0, y, im.width, y2))

	im.paste(Section, (a, y))

	for x in range(0,Section.width):
	    for y in range(0,Section.height):

	    	sectionpx = Section.load()

	    	R = sectionpx[ x, y ][0]
	        G = sectionpx[ x, y ][1]
	        B = sectionpx[ x, y ][2]	

	        R = 255-R
	        G = 255-G
	        B = 255-B

	        sectionpx[x,y] = (R, G, B)

im.show()