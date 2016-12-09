from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from math import floor

im = Image.open("scotch.jpg")
px = im.load()

im.crop(( 0, 0, 2448, 2448))

for x in range(0,im.width):
    for y in range(0,im.height):
    	if y < im.height/4:
    		px[x,y] = px[x-50,y]

        elif y > im.height/4 < im.height/2:
        	px[x,y] = px[x+50,y]

        elif y > im.height/2 < (im.height/2)*3:
        	px[x,y] = px[x-50]

        elif y > (im.height/2)*3:
        	px[x,y] = px[x+50,y]		

        	
       

im.show()
