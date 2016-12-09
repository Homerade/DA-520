import random
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from math import floor

im = Image.open("im_pancake.jpg")
px = im.load()

y1 = im.height/9
y2 = 200

rInt = random.randint(5,20)



# for x in range(0,im.width):
#     for y in range(0,im.height):
        
#         R = px[ x, y ][0]
#         G = px[ x, y ][1]
#         B = px[ x, y ][2]

# 	# 	ColorsOptions = [
# 	# 		['R=R/3', 'G=G-80', 'B=R'],	#green
# 	# 		['R=R-80', 'G=R', 'B=B/3'],	#grey
# 	# 		['R=B', 'G=G-80', 'B=B/3'],	#orange
# 	# 		['R=R/3', 'G=-80', 'B=G'],	#winter
# 	# 		['R=R/3', 'G=R', 'B=B-80'],	#deep blue
# 	# 		['R=R-80', 'G=G/3', 'B=G'],	#red
# 	# 	]

# 		# ColorShade = random.choice(ColorsOptions)	
#

#         #px[x,y] = ( ColorShade )


for y in range(0, im.height, im.height/9):  #im.height/rInt: 'rInt = random.randint(7,20)' random line thicknesses

	rIntX = random.randint(-(im.height-(im.height/9)),im.width)
	rIntY = random.randint(0,im.height)

	y = y + im.height/9
	y2 = y2 + im.height/9

	Section = im.crop(( 0, y, im.width, y2))

	im.paste(Section, (rIntX, rIntY))
               

im.show()