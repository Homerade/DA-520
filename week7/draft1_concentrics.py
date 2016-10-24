
from PIL import Image
from PIL import ImageDraw


im = Image.new("RGB", (1000,1000), (255,255,255))

draw = ImageDraw.Draw(im, 'RGBA')

data = [
	{'year' : 1820, 'figure' : 8385},
	{'year' : 1821, 'figure' : 9127},
	{'year' : 1822, 'figure' : 6911},
	{'year' : 1823, 'figure' : 6354},
	{'year' : 1824, 'figure' : 7912},
	{'year' : 1825, 'figure' : 10199},
	{'year' : 1826, 'figure' : 10837},
	{'year' : 1827, 'figure' : 18875},
]

x = (data[0]['year'])-1500
x2 = (data[1]['year'])-1500
x3 = (data[2]['year'])-1500
x4 = (data[3]['year'])-1500

draw.ellipse( (325,325,675,675), fill=(24, 109, 36), outline=(0,0,0)  )

draw.ellipse( (350,350,650,650), fill=(66, 116, 244), outline=(0,0,0) )

draw.ellipse( (450,450,550,550), fill=(244, 72, 66), outline=(0,0,0) )

# draw.ellipse( (x,x,450,450), fill=(2, 172, 6, 50), outline=(255,255,255) )
# draw.ellipse( (x2,x2,450,450), fill=(4, 7, 60, 50), outline=(255,255,255) )
# draw.ellipse( (x3,x3,450,450), fill=(24, 72, 16, 50), outline=(255,255,255) )
# draw.ellipse( (x4,x4,450,450), fill=(44, 27, 66, 50), outline=(255,255,255) )


im.show()

im.save("mydatavis.png")




# color =  figure [times] .01






