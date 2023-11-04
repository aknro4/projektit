import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from ucimlrepo import fetch_ucirepo

# fetch dataset
iris = fetch_ucirepo(id=2)

# data (as pandas dataframes)
X = iris.data.features
y = iris.data.targets

# Regression model
# metadata
# print(iris.metadata)

# variable information
# print(iris.variables)
