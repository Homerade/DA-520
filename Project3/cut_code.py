for y in range(0, im.height, im.height/9):
	for x in range(0, im.width):
		a = im.width/4
		a = a*(-1)

		y = y + im.height/9
		y2 = y2 + im.height/9

		Section = im.crop(( 0, y, im.width, y2))
		
			R = Section[ x, y ][0]
	        G = Section[ x, y ][1]
	        B = Section[ x, y ][2]

	        R = R
	        G = G - 100
	        B = B -100

	        Section[x,y] = ( R, G, B )

		im.paste(Section, (a, y))
               

im.show()

#################################