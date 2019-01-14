import mnist_loader
import network

#import data
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

#create network
net = network.Network([784,100,10])

#train network
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)