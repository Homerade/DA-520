
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


draw.polygon(((200,100),(300,200),(400,150)),outline=0, fill=0)


im.show()

im.save("mydatavis.png")






