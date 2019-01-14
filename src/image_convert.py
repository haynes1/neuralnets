import PIL as pillow
from PIL import Image

#get image
im = Image.open("../data/images/test0.jpg")

#crop image to square
width, height = im.size   # Get dimensions
min_dimension = min(width, height)
left = (width - min_dimension) / 2
top = (height - min_dimension) / 2
right = (width + min_dimension) / 2
bottom = (height + min_dimension) / 2
im.crop((left, top, right, bottom))

#make image grayscale
im = im.convert('L')

#make 28/28
im = im.resize((28,28), Image.ANTIALIAS)

#up the contrast
level = 140
factor = (259 * (level + 255)) / (255 * (259 - level))
def contrast(c):
    return 128 + factor * (c - 128)
im = im.point(contrast)

im.save("../data/images/test0-convert.jpg", "JPEG")