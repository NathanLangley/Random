import tensorflow as tf
import numpy as np
from keras import layers
import pandas as pd
from sklearn import model_selection
from statistics import mean
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-e", "--epoc", type=int, default=5000,
	help="# of epochs")
args = vars(ap.parse_args())


class ModelObj():
	def __init__(self):
		self.model = tf.keras.Sequential()
	def addDense(self, num_nodes):
		self.model.add(layers.Dense(num_nodes))
	def predict(self, inputs):
		return self.model.predict(inputs)
	def compile(self, optimizer = 'adam', loss = 'mae', metrics = ['mse', 'mae', 'mape']):
		self.model.compile(optimizer = optimizer,
              loss = loss,
              metrics = metrics)
	def fit(self, inputs, output, epoc = 100, verbose = 2):
		self.model.fit(inputs, output, epochs = args["epoc"], batch_size = len(inputs), verbose = 2)
	def save(self, direc):
		self.model.save(direc)
	def returnMod(self):
		return self.model


if __name__ == '__main__':
	db = pd.read_csv('temps.csv')

	db = pd.get_dummies(db)
	answer = np.array(db['actual'])
	answer_mod = answer#/float((max(answer)+1))
	db= db.drop('actual', axis = 1)
	db = np.array(db)


	train_features, test_features, train_labels, test_labels = model_selection.train_test_split(db, answer_mod, test_size = 0.3, random_state = 42)
	model = ModelObj()
	model.addDense(10)
	model.addDense(1)
	model.compile()
	model.fit(inputs = train_features, output = train_labels, epoc = args["epoc"])
	predicted = model.predict(test_features)
	model.save('models/tempModel')
	print("ACC: " + str(abs(((test_labels - predicted)).mean())))
	#print(test_features)
	#print(model.predict(test_features[0]))


	
