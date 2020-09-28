from numpy import array
from keras.models import Sequential
from keras.layers import Dense
from matplotlib import pyplot
import pandas as pd
import numpy as np
from sklearn import model_selection
import tensorflow as tf
# prepare sequence
#X = array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

db = pd.read_csv('temps.csv')

db = pd.get_dummies(db)
answer = np.array(db['actual'])
answer_mod = answer#/float((max(answer)+1))
db= db.drop('actual', axis = 1)
db = np.array(db)


train_features, test_features, train_labels, test_labels = model_selection.train_test_split(db, answer_mod, test_size = 0.1, random_state = 42)

# create model
model = Sequential()
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(1))
model.compile(loss='mae', optimizer='adam', metrics=['mae', 'mape'])
# train model
history = model.fit(train_features, train_labels, epochs=500, batch_size=len(train_labels), verbose=2)
# plot metrics
pyplot.plot(history.history['mae'])
pyplot.plot(history.history['mape'])
pyplot.show()
