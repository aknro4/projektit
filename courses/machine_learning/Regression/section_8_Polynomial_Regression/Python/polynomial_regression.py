import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Import data
dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Training the Linear Regression model
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Training the Polynomial regression model
# y = b_0 + b_1(x_n)^n. Degree means how many power of 'n' we go through.
# Higher n = higher accuracy, which means overfitting which we do not want that
# if n = 1 it is linear regression model
poly_reg = PolynomialFeatures(degree=4)
# simple matrix of features containing (x_n)
X_poly = poly_reg.fit_transform(X)
# Training part
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

plt.figure(figsize=(12, 7))
# Visualising Linear Regression model
plt.subplot(1,2,1)
plt.scatter(X, y, color="red")
plt.plot(X, lin_reg.predict(X), color="blue")
plt.title("Linear Regression model")
plt.xlabel("Position lvl")
plt.ylabel("Salary")

# Visualising Polynomial regression model
plt.subplot(1,2,2)
plt.scatter(X, y, color="red")
plt.plot(X, lin_reg_2.predict(X_poly), color="blue")
plt.title("Polynomial Regression model")
plt.xlabel("Position lvl")
plt.ylabel("Salary")

# Prevent overlapping
plt.tight_layout()
plt.show()

# Predicting new results whit linear regression
print(lin_reg.predict([[6.5]]))

# Predicting new results whit polynomial regression
print(lin_reg_2.predict(poly_reg.fit_transform([[6.5]])))
