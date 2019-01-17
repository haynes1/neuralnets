import mnist_loader
import network
import network2

#import data
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

#create network
net = network2.Network([784,30,10], cost=network2.CrossEntropyCost)

#train network
net.SGD(training_data, 30, 10, 0.5,
		lmbda = 5.0,
		evaluation_data=validation_data,
		monitor_evaluation_accuracy=True,
		monitor_evaluation_cost=True,
		monitor_training_accuracy=True,
		monitor_training_cost=True)

net.save("savednet.txt")