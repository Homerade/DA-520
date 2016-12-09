from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from math import floor
from PIL import gradientmask

im = Image.open("im_pancake.jpg")
px = im.load()

for x in range(0,im.width):
	for y in range(0, im.height):
		R = px[x,y][0]
		G = px[x,y][1]
		B = px[x,y][2]

		Red = R + 75
		Green = G - 30
		Blue = 30 - B

		px[x,y] = (Red,Green,Blue)

mask = gradientmask(im,0.5,1)

output = im.filter(ImageFilter.GaussianBlur(40))

output.paste(im,(0,0),mask)

output.show()		