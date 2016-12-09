from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from math import floor

im = Image.open("scotch.jpg")
px = im.load()



Section1 = im.crop(( 0, 0, im.width, 200))

im.paste(Section1, (200, 0))


Section2 = im.crop(( 0, 200, im.width, 400))

im.paste(Section2, (-200, 200))     
       

Section3 = im.crop(( 0, 400, im.width, 600))

im.paste(Section3, (200, 400)) 


Section4 = im.crop(( 0, 600, im.width, 800))

im.paste(Section4, (-200, 600)) 


Section5 = im.crop(( 0, 800, im.width, 1000))

im.paste(Section5, (200, 800)) 


Section6 = im.crop(( 0, 1000, im.width, 1200))

im.paste(Section6, (-200, 1000)) 


Section7 = im.crop(( 0, 1200, im.width, 1400))

im.paste(Section7, (200, 1200)) 


Section8 = im.crop(( 0, 1400, im.width, 1600))

im.paste(Section8, (-200, 1400)) 


Section9 = im.crop(( 0, 1600, im.width, 1800))

im.paste(Section9, (200, 1600)) 


Section10 = im.crop(( 0, 1800, im.width, 2000))

im.paste(Section10, (-200, 1800)) 


Section11 = im.crop(( 0, 2000, im.width, 2200))

im.paste(Section11, (200, 2000)) 

im.show()
