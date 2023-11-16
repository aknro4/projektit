import datetime
import random
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from tensorflow.keras.layers import Input, concatenate, Dense, Dropout
from tensorflow.keras.models import Model
import statsmodels.api as sm


# main dataset
dataset = pd.read_csv("f1db_csv/results.csv")

# Circuits for individual track training
circuits_dataset = pd.read_csv("f1db_csv/circuits.csv")
circuits_dataset = circuits_dataset[["circuitId"]].values

# Individual drivers for training
drivers_dataset = pd.read_csv("f1db_csv/drivers.csv")
drivers_dataset = drivers_dataset[["driverId"]].values

# Races dataset, way of getting circuitid
races_dataset = pd.read_csv("f1db_csv/races.csv")
# Get race id and remove it, instead we use circuitId
race_track_id = races_dataset[["raceId", "circuitId"]]
# Take track
dataset = dataset.merge(race_track_id, on="raceId", how="left")

# insert the new colum to index 2
dataset.insert(2, "circuitId", dataset.pop("circuitId"))

# According to F1 ESports professional modern era started 2014.
# So we will take all those races that started from 2014
race_date = races_dataset[["date", "raceId"]]
# Take the date
dataset = dataset.merge(race_date, on="raceId", how="left")
dataset['date'] = pd.to_datetime(dataset['date'], format='%Y-%m-%d')
# remove raceId, we use circuitId instead
dataset = dataset.drop(columns=["raceId"])

# print(len(dataset)) 9975
# Remove rows where year is not 2014 or higher
dataset = dataset[dataset['date'].dt.year >= 2014]
# Remove date. No need for that
dataset.pop("date")
# print(len(dataset)) 4091

# Remove all not needed columns, Not sure do we need position probably not.
dataset = dataset.drop(
    ["resultId", "number", "positionText", "points", "laps", "time", "milliseconds", "fastestLap", "rank",
     "fastestLapSpeed","statusId", "position"], axis=1)
print(dataset)

# save the data to csv
to_CSV = dataset
to_CSV.to_csv("training_sets/race_results", index=False)

# Features and independent variable
X = dataset.iloc[:, 0:4]
y = dataset.iloc[:, -2:]


# Dealing whit empty values '\N' by setting them to 0
y.replace(r"\\N", 0, inplace=True, regex=True)
X.replace(r"\\N", 0, inplace=True, regex=True)
X = X.values


# Function to convert time string to milliseconds
def time_string_to_milliseconds(time_string):
    if pd.notna(time_string) and time_string != 0:
        time_delta = datetime.datetime.strptime(time_string, "%M:%S.%f") - datetime.datetime(1900, 1, 1)
        milliseconds = int(time_delta.total_seconds() * 1000)
        return milliseconds
    else:
        return 0


# Function to convert milliseconds back to time string
def milliseconds_to_time_string(milliseconds_2d_array):
    time_strings_2d = []
    for row in milliseconds_2d_array:
        time_strings_row = []
        for milliseconds in row:
            if milliseconds != 0:
                milliseconds = int(milliseconds)
                time_delta = datetime.timedelta(milliseconds=milliseconds)
                time_string = (datetime.datetime(1900, 1, 1) + time_delta).strftime("%M:%S.%f")[:-3]
                time_strings_row.append(time_string)
            else:
                time_strings_row.append("0:00.000")
        time_strings_2d.append(time_strings_row)
    return time_strings_2d


# Changes minutes to milliseconds
y["fastestLapTime"] = y["fastestLapTime"].apply(time_string_to_milliseconds)

# Transform to same type as X
y = y.values

# Splitting the data into Training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature Scaling
sc_X = StandardScaler()
sc_y = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
y_train = sc_y.fit_transform(y_train)
y_test = sc_y.transform(y_test)

# Splitting predictions
y_test_time = y_test[:, 1]
y_train_time = y_train[:, 1]
y_test_position = y_test[:, 0]
y_train_position = y_train[:, 0]

# Training the TIME SVR model on the Training set
time_regressor = SVR(kernel='rbf', C=1.0, epsilon=0.1,)
time_regressor.fit(X_train, y_train_time)

# Predicting results adn validating results
y_pred_time = time_regressor.predict(X_test)
print(r2_score(y_test_time, y_pred_time))

# Add a constant term to X_train
X_train_const = sm.add_constant(X_train)
# Fit Ordinary Least Squares (OLS) regression using statsmodels
model_time = sm.OLS(y_train_time, X_train_const).fit()
# Print summary of the model
print(model_time.summary())

# Training the Position SVR model on the Training set
position_regressor = SVR(kernel='rbf', C=1.0, epsilon=0.1,)
position_regressor.fit(X_train, y_train_position)

# Predicting results
y_pred_position = position_regressor.predict(X_test)
print(r2_score(y_test_position, y_pred_position))

# Add a constant term to X_train
X_train_const = sm.add_constant(X_train)
# Fit Ordinary Least Squares (OLS) regression using statsmodels
model_position = sm.OLS(y_train_position, X_train_const).fit()
# Print summary of the model
print(model_position.summary())

