from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from math import floor

im = Image.open("im_pancake.jpg")
px = im.load()

y1 = im.height/9
y2 = 200

for x in range(0,im.width):
    for y in range(0,im.height):
        # Retriev the Red, Green and Blue value of the pixel
        R = px[ x, y ][0]
        G = px[ x, y ][1]
        B = px[ x, y ][2]

		# Do something amazing here to change R G and B!
        R = R
        G = R
        B = B

		# Now we use our new R G B values to update the pixel.
        px[x,y] = ( R, G, B )

        a = im.width/4
        a = a*(-1)

        y = y + im.height/9
        y2 = y2 + im.height/9

        Section = im.crop(( 0, y, im.width, y2))

        im.paste(Section, (a, y))

im.show()
