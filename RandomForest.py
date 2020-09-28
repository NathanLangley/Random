import pandas as pd
import numpy as np
from sklearn import *

db = pd.read_csv('temps.csv')

db = pd.get_dummies(db)


# Labels are the values we want to predict
answer = np.array(db['actual'])
# Remove the labels from the features
# axis 1 refers to the columns
db= db.drop('actual', axis = 1)
# Saving feature names for later use
data_names = list(db.columns)
# Convert to numpy array
db = np.array(db)

train_features, test_features, train_labels, test_labels = model_selection.train_test_split(db, answer, test_size = 0.2, random_state = 42)


rf = ensemble.RandomForestRegressor(n_estimators = 1000, random_state = 42)

# Train the model on training data
rf.fit(train_features, train_labels);
feature_importances = (rf.feature_importances_)
feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(data_names, feature_importances)]

feature_importances = sorted(feature_importances, key = lambda x:x[1], reverse = True)
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances]
predictions = rf.predict(test_features)
# Calculate the absolute errors
errors = abs(predictions - test_labels)
print(round(np.mean(errors),3))
