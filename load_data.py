import csv

def load_data_as_array(path):

#Loads csv files into arrays

	data = []

	if isinstance(path, str) is False:

		path = str(path)


	ifile  = open(path, "r")

	read = csv.reader(ifile)

	for row in read :
		data.append(row)

	return data