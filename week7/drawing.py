# First, install Pillow in your Terminal:   pip install pillow

# Import two modules from Pillow: Image and ImageDraw
from PIL import Image
from PIL import ImageDraw

# Create a new image with 1000px width, 500px height, and a white background
im = Image.new( "RGB", (1000,500), (255,255,255) )
# Activate the ability to draw on our image.
draw = ImageDraw.Draw( im, 'RGBA' )

# DRAW HERE!
# Draw a circle. First parameter is x/y coordinates, second parameter is color (see video lesson).
draw.ellipse( (0,0,100,100), fill=(0,100,200,50) )
draw.line( (0,200,300,200), fill=0, width=3 )


# Preview the image
im.show()
# Save the image
im.save("mydatavis.png")
