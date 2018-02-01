#load test and train data

from load_data import load_csv_as_array
import numpy as np

test_data = load_csv_as_array("fashion-mnist_test.csv")
train_data = load_csv_as_array("fashion-mnist_train.csv")


testY = test_data[:,0]

trainY = train_data[:,0]


#Scale the data between 0-1

testX = test_data[:,1:]/255

trainX = train_data[:,1:]/255

print("There are these many examples in test set:", testY.shape[0])
print("There are these many examples in train set:", trainY.shape[0])
print("There are these many pixels per example:", testX.shape[1])