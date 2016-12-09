
Section = im.crop(( im.width/4, 0, (im.width/4)*3, 50))

im.paste(Section (im.width/4)+200, 0))  

#######################

startX = im.width/4     	
endX = startX*3

yPortion = 0
yPortion = yPortion + 200


Section1 = im.crop(( startX, yPortion, endX, yPortion))

im.paste(Section1, (startX+200, yPortion))       	
       

im.show()

########################

startX = im.width/4     	
endX = startX*3

startY = 0
endY = startY + 200

for x in range(0, im.width):
	for y in range(0, im.height):
		Section = im.crop(( startX, startY, endX, endY))
		im.paste(Section, (startX+200, endY)) 

########################

startX = im.width/4     	
endX = startX*3

startY = 0
endY = 200

for y in range(0, im.height,200):

	startY = startY+200
	endY = endY+200 

	Section = im.crop(( startX, y, endX, y))
	im.paste(Section, (startX+200, endY)) 

#########################

for y in range(0, im.height, im.height/9):

	a = im.width/4
	a = a*(-1)

	Section = im.crop(( 0, y, im.width, y))

	im.paste(Section, (a, y))


###########################

im = Image.open("scotch.jpg")
px = im.load()

y1 = 0
y2 = im.height/9

for y in range(0, im.height, im.height/9):

	a = 200
	a = a*(-1)

	y1 = y1 + im.height/9
	y2 = y2 + im.height/9

	Section = im.crop(( 0, y1, im.width, y2))

	im.paste(Section, (a, y1))
               

im.show()





	

