import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Import data
dataset = pd.read_csv("Salary_Data.csv")
# matrix of features or independent values
X = dataset.iloc[:, :-1].values
# matrix of dependent variable vector
y = dataset.iloc[:, -1].values

# Split data to Test set and training set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Training simple linear regression on the training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test results
y_pred = regressor.predict(X_test)
# print(y_pred)

# Get single prediction Ex. from Person who has 12 years of experience.
print(regressor.predict([[12]]))

# Visualising Training set results
plt.scatter(X_train, y_train, color="red")
plt.plot(X_train, regressor.predict(X_train), color="blue")
plt.title("Years of Experience vs Salary (Training set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

# Visualising Test set results
plt.scatter(X_test, y_test, color="red")
# No need to change these. The result will be the same regardless because of the unique equation, and
# we would end up whit same regression line.
plt.plot(X_train, regressor.predict(X_train), color="blue")
plt.title("Years of Experience vs Salary (Test set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
