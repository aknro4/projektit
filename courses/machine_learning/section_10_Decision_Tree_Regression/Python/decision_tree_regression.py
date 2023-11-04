import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

# Import data
dataset = pd.read_csv("Position_Salaries.csv")

# Extracting features "Independent" (X) and dependent variable (y)
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Fitting the regression model to the dataset
regressor = DecisionTreeRegressor(max_depth=2)
regressor_1 = DecisionTreeRegressor(max_depth=5)
regressor.fit(X, y)
regressor_1.fit(X, y)

# Predicting new result with regression model
y_pred = regressor.predict([[6.5]])
y_pred_1 = regressor_1.predict([[6.5]])
print(y_pred)
print(y_pred_1)

# Visualizing regression model
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color="red", label="Data")
# 'X_grid' gives low-res and 'X' gives high-res graph
plt.plot(X_grid, regressor.predict(X_grid), label="max_depth=2", color="blue")
plt.plot(X_grid, regressor_1.predict(X_grid), label="max_depth=5", color="green")
plt.title("Decision Tree Model")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.legend()
plt.show()
