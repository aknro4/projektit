import datetime
import random
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv("f1db_csv/qualifying.csv")
races_dataset = pd.read_csv("f1db_csv/races.csv")
# Get race id and remove it, instead we use circuitId
race_track_id = races_dataset[["raceId", "circuitId"]]
# Acording to F1 ESports professional modern era started 2014.
# So we will take all those races that started from 2014
race_date = races_dataset[["date", "raceId"]]
dataset = dataset.merge(race_date, on="raceId", how="left")
dataset = dataset.merge(race_track_id, on="raceId", how="left")
dataset = dataset.drop(columns=["raceId"])
dataset['date'] = pd.to_datetime(dataset['date'], format='%Y-%m-%d')
# insert the new colum to index 2
dataset.insert(2, "circuitId", dataset.pop("circuitId"))

# print(len(dataset)) 9975
# Remove rows where year is not 2014 or higher
dataset = dataset[dataset['date'].dt.year >= 2014]
# Remove date. No need for that
dataset.pop("date")
# print(len(dataset)) 4091

# Ehh I guess we could predict position as well.
# dataset = dataset.drop(["number", "position"], axis=1)
X = dataset.iloc[:, 1:-5].values
y = dataset.iloc[:, -3:]

# Dealing whit empty values '\N' by setting them to 0
y.replace(r"\\N", 0, inplace=True, regex=True)


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
y_test = sc_y.transform(y_test)


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


# Initial model: Create a simple regression model
initial_model = tf.keras.Sequential([
    tf.keras.layers.Dense(100, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(100, activation='relu', name='hidden_layer_1'),
    tf.keras.layers.Dropout(0.2),  # Adding dropout for regularization
    tf.keras.layers.Dense(3, activation='linear')
])

# Compile the model using the custom loss function and custom learning rate
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)  # Adjust the learning rate as needed
initial_model.compile(optimizer=optimizer, loss=custom_loss, metrics=['mae'])
# Train the model
# epochs: number of iterations over the entire training set
# batch_size: NUmber of samples used in each iteration for updating the models weights.
initial_model.fit(X_train, y_train, epochs=200, batch_size=20, validation_data=(X_test, y_test))

# Second model
# Use the initial model to make predictions on the training set
predicted_q2q3 = initial_model.predict(X_train)
predicted_q2q3 = sc_y.inverse_transform(predicted_q2q3)
predicted_q2q3[predicted_q2q3 < 5000] = 0

print(predicted_q2q3)
predicted_q2q3 = sc_y.transform(predicted_q2q3)

# Create a mask to filter out rows where q2 or q3 is predicted as 0
mask_q2 = predicted_q2q3[:, 1] != 0
mask_q3 = predicted_q2q3[:, 2] != 0

# Apply the masks to exclude rows with true 0 values
X_train_stacked = np.concatenate((X_train[mask_q2 & mask_q3], predicted_q2q3[mask_q2 & mask_q3]), axis=1)
y_train_stacked = y_train[mask_q2 & mask_q3]

print(X_train_stacked.shape)
print(y_train_stacked.shape)

second_model = tf.keras.Sequential([
    tf.keras.layers.Dense(6, activation='relu', input_shape=(X_train_stacked.shape[1],)),
    tf.keras.layers.Dense(100, activation='relu', name='hidden_layer_1'),
    tf.keras.layers.Dense(100, activation='relu', name='hidden_layer_2'),
    tf.keras.layers.Dropout(0.2),  # Adding dropout for regularization
    tf.keras.layers.Dense(3, activation='linear')
])

# Compile the model using the custom loss function and custom learning rate
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)  # Adjust the learning rate as needed
second_model.compile(optimizer=optimizer, loss=custom_loss, metrics=['mae'])

# Train the second model
second_model.fit(X_train_stacked, y_train_stacked[:, 1], epochs=100, batch_size=20,
                 validation_data=(X_test, y_test[:, 1]))


# Check predictions
y_pred = second_model.predict(X_test)
y_pred = sc_y.inverse_transform(y_pred)
# If the prediction is less than 5s I consider that as a 0. Should be larger thought
y_pred[y_pred < 5000] = 0

# Inverse transform
X_test = sc_X.inverse_transform(X_test)
y_test = sc_y.inverse_transform(y_test)

# Comparing predictions
a = random.randint(1, 250)
print(X_test[a:a + 15])
print(milliseconds_to_time_string(y_pred[a:a + 15]), "\nTrue values")
print(milliseconds_to_time_string(y_test[a:a + 15]))

# Evaluate the Model Performance
r2 = r2_score(y_test, y_pred)
print("R2 score: ", r2)

second_model.save('models/modern_f1_era_quali_model.keras')

# Single value prediction
# first value is driver, second value is track, constructor is third
single_input = np.array([[64, 8, 28], [817, 71, 9]])
single_input_standardized = sc_X.transform(single_input)
predicted_output_standardized = second_model.predict(single_input_standardized)
predicted_output = sc_y.inverse_transform(predicted_output_standardized)

# Print the predictions
print(X_test[[15]], X_test[[60]])
print("True values: \n", y_test[15], y_test[60])
predicted_output[predicted_output < 0] = 0
print(milliseconds_to_time_string([y_test[15]]), milliseconds_to_time_string([y_test[60]]))
print("Predictions : \n", predicted_output, "\n", milliseconds_to_time_string(predicted_output))
