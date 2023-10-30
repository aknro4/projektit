import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

data_csv = "Data.csv"
dataset = pd.read_csv(data_csv)

# Matrix of features and dependent viable vector
# Data to learn from (features), take all data expect last column
X = dataset.iloc[:, :-1].values
# Data to predict (dependent variable vector), take all data from last column
y = dataset.iloc[:, -1].values
print("Matrix Features \n", X, "\n")
print("Matrix dependent variable vector \n", y, "\n")

# Count how many empty values
# counter = 0
# for i in X[:, 1:3]:
#     if np.isnan(i[0]):
#         counter += 1
#     if np.isnan(i[1]):
#         counter += 1
# print(counter)

# Or simply / easier. Produces an error
# empty_data = np.isnan(X[:, 1:3])
# total_empty_values = sum(empty_data)
# print(total_empty_values)

# Or
total_empty_values = pd.isna(X[:, 1:3]).sum()
print("Empty values ", total_empty_values, "\n")

# Handling missing data
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
# Find missing values (Only numeric values)
imputer.fit(X[:, 1:3])
# Replace missing values
X[:, 1:3] = imputer.transform(X[:, 1:3])
print("Handling missing data \n", X, "\n")

# Encoding categorical data Example: Spain, France, Germany
# Spain = 0 0 1, France = 0 1 0, Germany = 1 0 0
# one hot encoding
ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [0])], remainder="passthrough")
X = np.array(ct.fit_transform(X))
print("Encoding categorical data \n", X, "\n")

# Encoding dependent variable
le = LabelEncoder()
y = le.fit_transform(y)
print("Encoding dependent variable \n", y, "\n")
