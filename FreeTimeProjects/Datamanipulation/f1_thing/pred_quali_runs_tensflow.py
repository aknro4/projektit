import datetime
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.multioutput import MultiOutputRegressor
from sklearn.svm import SVR

dataset = pd.read_csv("f1db_csv/qualifying.csv")
races_dataset = pd.read_csv("f1db_csv/races.csv")
# Get race id and remove it, instead we use circuitId
race_track_id = races_dataset[["raceId", "circuitId"]]
dataset = dataset.merge(race_track_id, on="raceId", how="left")
dataset = dataset.drop(columns=["raceId"])
# insert the new colum to index 2
dataset.insert(2, "circuitId", dataset.pop("circuitId"))

# Ehh I guess we could predict position as well.
# dataset = dataset.drop(["number", "position"], axis=1)
X = dataset.iloc[:, 1:-5].values
y = dataset.iloc[:, -3:]

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


y = y.applymap(time_string_to_milliseconds)

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


# Initial Training
# Define custom loss function
# Some notes about this function
# threshold_milliseconds: Threshold value, max allowable difference between true and predicted value, 200 seems ok
# tf.where is used to create a tensor by choosing elements from two tensors based on a condition
# in this case error <= threshold_milliseconds
def custom_loss(y_true, y_pred, threshold_milliseconds=200):
    # y_pred = tf.cast(y_pred, dtype=tf.int64)  # Cast y_pred to int64
    y_true = tf.cast(y_true, dtype=tf.float32)  # Cast y_true to float32
    # Absolute difference between true and predicted values
    error = tf.abs(y_true - y_pred)
    penalty = tf.where(error <= threshold_milliseconds,
                       0.1 * tf.math.pow(error / threshold_milliseconds, 2),  # Quadratic penalty term
                       error - 0.1 * threshold_milliseconds)  # Linear penalty term
    return tf.reduce_mean(penalty)


# Create a simple regression model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(100, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(125, activation='relu', name='hidden_layer_1'),
    tf.keras.layers.Dense(70, activation='relu', name='hidden_layer_2'),
    tf.keras.layers.Dense(3, activation='linear')  # The 3 values to predict
])

# Compile the model using the custom loss function
model.compile(optimizer='adam', loss=custom_loss, metrics=['mae'])
# Train the model
# epochs: number of iterations over the entire training set
# batch_size: NUmber of samples used in each iteration for updating the models weights.
model.fit(X_train, y_train, epochs=125, batch_size=32, validation_data=(X_test, y_test))

# Second model SOON TM

# Check predictions
y_pred = model.predict(X_test)
y_pred = sc_y.inverse_transform(y_pred)
y_pred[y_pred < 0] = 0
# Comparing predictions
print(y_pred[:5], "\n")
print(y_test[:5])

# Single value prediction
# first value is driver, second value is track, constructor is third
single_input = np.array([[64, 8, 28], [817, 71, 9],[102,8,131]])
single_input_standardized = sc_X.transform(single_input)
predicted_output_standardized = model.predict(single_input_standardized)
predicted_output = sc_y.inverse_transform(predicted_output_standardized)

# Print the predictions
print(sc_X.inverse_transform(X_test[[15]]), sc_X.inverse_transform(X_test[[60]]))
print("True values: \n", y_test[15], y_test[60])
predicted_output[predicted_output < 0] = 0
print("Predictions : \n", predicted_output)

# Evaluate the Model Performance
r2 = r2_score(y_test, y_pred)
print("R2 score: ", r2)

# Some tough's
# Currently our model is pretty damn close to perfect predicting values that are 0
# BUT, it does lack when trying to predict second and third values
# That might be because of the inbetween the correct value and the 0 value.
# And thus wants to predict in between 0 and true value.
# Which we can use to calculate % and get chance of the driver to get time in quali


# Here are some outputs

# True values:
# [84184     0     0] [98091 97569 97125]

# Predictions :
# [[85442.92      0.        0.   ]
# [90313.72  74549.47  44950.223]]

# If we calculate 74549.47/97569 we would geet the % change of the driver getting a time in second quali.
# And same for third.
# I would love to know a way to predict time based on these %


# Later implementation
# Create more models to predict values from initial models predictions
# FOR SECOND MODEL
#   look at all the values. And predict those values based on the initial models predictions
#   We ignore values that already are 0
# THIRD MODEL
#   Only look at the predicted values from the second model.
#   AND make new prediction based on those predictions
#
# Finally our final model will be third model. That we use to predict values?
# Or I don't know im not good at this
