from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from math import floor

im = Image.open("im_scotch.jpg")
px = im.load()

y1 = im.height/9
y2 = 200


for y in range(0, im.height, im.height/9):

	a = im.width/4
	a = a*(-1)

	y = y + im.height/9
	y2 = y2 + im.height/9

	Section = im.crop(( 0, y, im.width, y2))

	im.paste(Section, (a, y))
               

im.show()