#load test and train data

from load_data import load_csv_as_array

test_data = load_csv_as_array("fashionmnist/fashion-mnist_test.csv")
train_data = load_csv_as_array("fashionmnist/fashion-mnist_train.csv")

