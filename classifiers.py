import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Maxpooling2D, Flatten
from keras.applications.resnet50 import ResNet50
#from keras.applications.resnet50 import preprocess_input, decode_predictions

from keras.models import Model


#def resnetClassifier(input_shape):

# 	model = ResNet50(weights = 'imagenet', include_top = False)

# img = image.load_img(img_path, target_size=(224, 224))
# x = image.img_to_array(img)
# x = np.expand_dims(x, axis=0)
# x = preprocess_input(x)

# preds = model.predict(x)
# # decode the results into a list of tuples (class, description, probability)
# # (one such list for each sample in the batch)
# print('Predicted:', decode_predictions(preds, top=3)[0])

class simpleCNN(alpha, input_shape):

	model = Sequential()
	model.add(Conv2D(28, (3, 3), strides=(2,2), activation='softplus',
					input_shape=input_shape))
	model.add(Conv2D(14, (3, 3), strides=(2,2), activation='softplus'))
	model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

	model.add(Flatten())

	model.add(Dense(128, activation='softplus', kernel_regularizer=l2(alpha)))
	model.add(Dense(32, activation='softplus'))
	model.add(Dense(10, activation='softplus'))


	def __init__(self):

		optimizer = Adam(lr = .0001, decay = 5e-5)
		self.model.compile(optimizer=optimizer,
		loss='sparse_categorical_crossentropy',
		metrics=['accuracy'])

		return self.model

	def fitSimpleCNN(self, model, trainX, trainY, validX, validY,
						epochs = 10, batch_size = 512):

		

		

		return self.model


