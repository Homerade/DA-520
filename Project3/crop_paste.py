from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from math import floor

im = Image.open("scotch.jpg")
px = im.load()


# for x in range(0,im.width):
#     for y in range(0,im.height):
    	
startX = im.width/4     	
endX = startX*3

startY = 0
endY = startY + 200


Section1 = im.crop(( startX, startY, endX, endY))

im.paste(Section1, (startX+200, startY))       	
       

im.show()
