import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression

# Import data
dataset = pd.read_csv("50_Startups.csv")
# Features or independent values
X = dataset.iloc[:, :-1].values
# dependent vector
y = dataset.iloc[:, -1].values

# Encoding dummy values.
ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [3])], remainder="passthrough")
X = np.array(ct.fit_transform(X))
# print(X)

# Split data to Test set and training set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Training multiple linear processing on the training set.
# Whit Linearregression() no need to worry about "dummy trap" or
# worry about selecting best features aka values whit highest P-value. It does them for you.
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting test set results
y_pred = regressor.predict(X_test)
# Accuracy up to 2 decimals
np.set_printoptions(precision=2)
# Reshaping horizontal vector vertically whit one colum.
# Showing predicted results on the left and actual results on the right
# We do this to value how good our model is for the data set.
# Obviously you would compare all the results from different models.
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

# Predict single prediction.
print("Single prediction ", regressor.predict([[1, 0, 0, 160000, 130000, 300000]]))
