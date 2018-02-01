import pandas as pd
import numpy as np


def load_csv_as_array(path):

#Loads csv files into numpy arrays as float32

	if isinstance(path, str) is False:

		path = str(path)


	data = pd.read_csv(path)

	npdata = np.array(data, dtype = 'float32')

	return npdata