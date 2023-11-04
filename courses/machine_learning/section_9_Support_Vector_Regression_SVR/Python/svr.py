import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

# Import data
dataset = pd.read_csv("Position_Salaries.csv")

# Extracting features (X) and independent variable (y)
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, -1].values

print("Features \n", X, "\n Independent variable \n", y)

# Reshaping y from 1D array to 2D array
y = y.reshape(len(y), 1)
print("Independent variable after reshape \n", y)

# Feature scaling Notes:
# We do not need to apply feature scaling on dummy values. Because they are already in right range(0 to 1)
# If independent variable is not in the same range as features, features AND independent variables must be scaled
# Feature scaling should be applied after splitting the data into training set and test set

# Feature scaling implementation
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

print("Features after Scaling \n", X, "\n and Independent variable \n", y)

# Fitting the regression model to the dataset
regressor = SVR(kernel="rbf")
regressor.fit(X, y)

# Predicting new result with regression model
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform([[6.5]])).reshape(-1, 1))
print("Prediction: ", y_pred)

plt.figure(figsize=(12, 7))
# Visualizing regression model
plt.subplot(1, 2, 1)
plt.scatter(sc_X.inverse_transform(X),
            sc_y.inverse_transform(y),
            color="red")
plt.plot(sc_X.inverse_transform(X),
         sc_y.inverse_transform(regressor.predict(X).reshape(-1, 1)),
         color="blue")
plt.title("SVR Regression Model (Low Res)")
plt.xlabel("Level")
plt.ylabel("Salary")

# High resolution
plt.subplot(1, 2, 2)
# Probably should inverse transform in this step and not later on.
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(sc_X.inverse_transform(X),
            sc_y.inverse_transform(y),
            color="red")
plt.plot(sc_X.inverse_transform(X_grid),
         sc_y.inverse_transform(regressor.predict(X_grid).reshape(-1, 1)),
         color="blue")
plt.title("SVR Regression Model (High Res)")
plt.xlabel("Level")
plt.ylabel("Salary")

plt.tight_layout()
plt.show()
