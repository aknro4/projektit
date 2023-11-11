import datetime
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score, classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

dataset = pd.read_csv("f1db_csv/qualifying.csv")
races_dataset = pd.read_csv("f1db_csv/races.csv")
# Get race id and remove it, instead we use circuitId
race_track_id = races_dataset[["raceId", "circuitId"]]
dataset = dataset.merge(race_track_id, on="raceId", how="left")
dataset = dataset.drop(columns=["raceId"])

dataset.insert(2,"circuitId",dataset.pop("circuitId"))
# Ehh I guess we could predict position as well.
# dataset = dataset.drop(["number", "position"], axis=1)
X = dataset.iloc[:, 1:-5].values
y = dataset.iloc[:, -3:]
print(X)

# Dealing whit empty values '\N'
y.replace(r"\\N", 0, inplace=True, regex=True)


# Function to convert time string to milliseconds
def time_string_to_milliseconds(time_string):
    if pd.notna(time_string) and time_string != 0:
        time_delta = datetime.datetime.strptime(time_string, "%M:%S.%f") - datetime.datetime(1900, 1, 1)
        milliseconds = int(time_delta.total_seconds() * 1000)
        return milliseconds
    else:
        return 0


y = y.map(time_string_to_milliseconds)
# Transform to same type as X
y = y.values

# Splitting the data into Training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

print(X_test[15])
print(y_test[15])

# Feature Scaling
sc_X = StandardScaler()
sc_y = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
y_train = sc_y.fit_transform(y_train)

# Training the SVR model on the Training set
# The problem with this is that if the model does not get exact prediction correct, it will penalize itself
# And thus, predictions will be inaccurate
svr = SVR(kernel='rbf')
multioutput_regressor = MultiOutputRegressor(svr)
multioutput_regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = multioutput_regressor.predict(X_test)
y_pred = sc_y.inverse_transform(y_pred)
y_pred[y_pred < 0] = 0

# Printing predictions
print(y_pred[:10], "\n", y_test[:10])

# Predicting from single input
new_pred = multioutput_regressor.predict([[64, 8, 28]])
new_pred = sc_y.inverse_transform(new_pred)
print(new_pred)

# Evaluating the Model Performance
r2 = r2_score(y_test, y_pred)

print("R2 score: ", r2)