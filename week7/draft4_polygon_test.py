
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

x = (data[0]['year'])
y = (data[0]['figure'])*.1

# x2 = (data[1]['year'])
# x3 = (data[2]['year'])
# x4 = (data[3]['year'])


# draw.arc((0,0,500,500),0,50,fill=0)
# draw.arc((10,10,510,510),0,350,fill=50)
# draw.arc((20,20,520,520),0,100,fill=100)
# draw.arc((30,30,530,530),0,250,fill=150)
# draw.arc((40,40,540,540),0,177,fill=200)
# draw.arc((50,50,550,550),0,44,fill=250)


# distance from the last year = difference between figure from previous year
# arc = ratio of figure on 0-360 scale
# color = progressing RGB
#make it go in a circle instead of a diagonal line

draw.polygon(((200,100),(300,200),(400,150)),fill=0)

im.show()

im.save("mydatavis.png")




# color =  figure [times] .01
# parabola curves up at a distance of the difference from the year before






