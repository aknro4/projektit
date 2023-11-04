import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Import data
dataset = pd.read_csv("data.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Encoding dummy values
# ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [3])], remainder="passthrough")
# X = np.array(ct.fit_transform(X))

# Split data to Test set and training set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
