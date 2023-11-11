from sklearn.compose import ColumnTransformer
from sklearn.datasets import fetch_openml
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import numpy as np
import pandas as pd

# Fetch dataset
iris = fetch_openml(name='iris')

# data (as pandas dataframes)
X = iris.data
y = iris.target

# No one-hot encoding for SVR
y = pd.Categorical(y).codes

# Splitting data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature Scaling for input features
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Training the model
regressor = SVR(kernel='rbf')
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Print the predicted and true values
np.set_printoptions(precision=2)
print("Predicted and true value")
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

# Evaluating the Model
r2 = r2_score(y_test, y_pred)
print("R2 Score:", r2)
