import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Import data
dataset = pd.read_csv("Position_Salaries.csv")

# Extracting features "Independent" (X) and dependent variable (y)
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Fitting the Random Trees regression model to the dataset
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X, y)

# Predicting new result with regression model
# No trasformation method needed because we did not use feature scaling this time
y_pred = regressor.predict([[6.5]])
print(y_pred)

# Visualizing regression model
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color="red", label="Data")
# 'X_grid' gives low-res and 'X' gives high-res graph
plt.plot(X_grid, regressor.predict(X_grid), label="max_depth=2", color="blue")
plt.title("Random Tree Model")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.legend()
plt.show()
