from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from math import floor

im = Image.open("im_sidewalk.jpg")
px = im.load()

for x in range(0,im.width):
    for y in range(0,im.height):
        # Retriev the Red, Green and Blue value of the pixel
        R = px[ floor(x/15), y ][0]
        G = px[ floor(x/10)*10, y ][1]
        B = px[ x, y ][2]

		# Do something amazing here to change R G and B!
	if G < 110:
		R = 200
		G = 180
		B = 145

	else:
		R = 10 
		G = R	
		B = 0


		# Now we use our new R G B values to update the pixel.
        px[x,y] = ( R, G, B )

im.show()
