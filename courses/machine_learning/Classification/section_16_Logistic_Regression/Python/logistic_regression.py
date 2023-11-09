import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# Import data
dataset = pd.read_csv("Social_Network_Ads.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Split data to Test set and training set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training Logistic Regression model on the training set
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# Predicting single value,
# remember to SCALE the single values to same SCALE as the TRAINING set.
print(classifier.predict(sc.transform([[30, 87000]])))

# Predict
y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred), 1),
                      y_test.reshape(len(y_test), 1)), 1))

# Confusion matrix
print(confusion_matrix(y_pred,y_test))
