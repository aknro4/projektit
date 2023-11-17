from sklearn.preprocessing import StandardScaler
from ucimlrepo import fetch_ucirepo
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import r2_score
import statsmodels.api as sm
import random
from joblib import dump, load


# fetch dataset
wine = fetch_ucirepo(id=109)

# data (as pandas dataframes)
X = wine.data.features
y = wine.data.targets

to_CSV = X
to_CSV.to_csv("training_data/X_wine.csv", index=False)

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Get some single predictions
a = random.randint(0, 20)
print(X_test.iloc[a])
# I don't even know should I scale the values after getting 1.0 R2 rating
# sc_X = StandardScaler()
# sc_y = StandardScaler()

# Training the Random Forest Classifier model on the whole dataset
# I guess sometimes it to be really simple
classifier = RandomForestClassifier(n_estimators=5, random_state=0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
# Probabilities
y_proba = classifier.predict_proba(X_test)
print(y_proba)

# Evaluating the Model Performance
r2 = r2_score(y_test, y_pred)
print(r2)
# Additional performance evaluation
# Add a constant term to X_train
X_train_const = sm.add_constant(X_train)
# Fit Ordinary Least Squares (OLS) regression using statsmodels
model = sm.OLS(y_train, X_train_const).fit()
# Print summary of the model
print(model.summary())

# Single prediction
# need to convert the data to df first....
data_to_predict = [[13.0, 5.80, 2.13, 21.50, 86.00, 2.62, 2.65, 0.30, 2.01, 2.60, 0.73, 3.10, 380.00]]
df = pd.DataFrame(data_to_predict, columns=["Alcohol","Malicacid","Ash","Alcalinity_of_ash","Magnesium", "Total_phenols",
                                            "Flavanoids","Nonflavanoid_phenols","Proanthocyanins","Color_intensity","Hue",
                                            "0D280_0D315_of_diluted_wines","Proline"])

# Make single prediction
single_pred = classifier.predict(df)
single_pred_proba = classifier.predict_proba(df)

# Print prediction
print(single_pred)
print(single_pred_proba)

dump(classifier,"model/RFC_Wine.joblib")
