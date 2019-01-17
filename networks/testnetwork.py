import network2
from PIL import Image
import numpy as np
import mnist_loader

#converts from 0 - 255 to 1 - 0
def convertImage(x):
	return abs((x - 255) / -255)


#load network
net = network2.load("savednet.txt")


#import data
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

print training_data[0]




#load test image
img = Image.open("../data/images/test0-convert.jpg")
img.load()
data = np.asarray( img, dtype="float")

flattened = convertImage(np.reshape(data, (np.product(data.shape),1)))
print flattened, flattened.shape


result = net.feedforward(flattened)

print result
