from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from math import floor

im = Image.open("landscape.jpg")
px = im.load()

for x in range(0,im.width):
    for y in range(0,im.height):
        # Retriev the Red, Green and Blue value of the pixel
        R = px[ x, y ][0]
        G = px[ x, y ][1]
        B = px[ x, y ][2]

		# Do something amazing here to change R G and B!





		# Now we use our new R G B values to update the pixel.
        px[x,y] = ( R, G, B )

im.show()
