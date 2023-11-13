import datetime
import random
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.layers import Input, concatenate, Dense, Dropout
from tensorflow.keras.models import Model

dataset = pd.read_csv("f1db_csv/qualifying.csv")
races_dataset = pd.read_csv("f1db_csv/races.csv")
# Get race id and remove it, instead we use circuitId
race_track_id = races_dataset[["raceId", "circuitId"]]
# According to F1 ESports professional modern era started 2014.
# So we will take all those races that started from 2014
race_date = races_dataset[["date", "raceId"]]
# Take the date
dataset = dataset.merge(race_date, on="raceId", how="left")
# Take track
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


# Recommends map instead of appymap
y = y.applymap(time_string_to_milliseconds)

# Transform to same type as X
y = y.values

# Splitting the data into Training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

print(y_train)
print(X_train)

# Feature Scaling
sc_X = StandardScaler()
sc_y = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
y_train = sc_y.fit_transform(y_train)
y_test = sc_y.transform(y_test)

# Train first whit only tracks
X_train_tracks = X_train[:, 1:2]
X_test_tracks = X_test[:, 1:2]


# Define custom loss function
# Some notes about this function
# threshold_milliseconds: Threshold value, max allowable difference between true and predicted value, 200 seems ok
# tf.where is used to create a tensor by choosing elements from two tensors based on a condition
# in this case error <= threshold_milliseconds
def custom_loss(y_true, y_pred, threshold_milliseconds=200):
    y_true = tf.cast(y_true, dtype=tf.float32)  # Cast y_true to float32
    error = tf.abs(y_true - y_pred)

    # Quadratic penalty term for values close to zero.
    quadratic_penalty = tf.where((y_true != -1.59967049) & (y_true != -0.93527763) & (error <= threshold_milliseconds),
                                 0.1 * tf.math.pow(error / threshold_milliseconds, 2),
                                 0.0)

    # Linear penalty term for other values
    linear_penalty = tf.where((y_true != -1.59967049) & (y_true != -0.93527763) & (error > threshold_milliseconds),
                              error - 0.1 * threshold_milliseconds,
                              0.0)

    return tf.reduce_mean(quadratic_penalty + linear_penalty)


# Track model: Trains based on only tracks
track_model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train_tracks.shape[1],),
                          kernel_regularizer=tf.keras.regularizers.l2(0.01),
                          kernel_initializer='he_normal'),
    tf.keras.layers.Dense(64, activation='relu', name='hidden_layer_1',
                          kernel_regularizer=tf.keras.regularizers.l2(0.01),
                          kernel_initializer='he_normal'),
    tf.keras.layers.Dense(64, activation='relu', name='hidden_layer_2',
                          kernel_regularizer=tf.keras.regularizers.l2(0.01),
                          kernel_initializer='he_normal'),
    tf.keras.layers.Dropout(0.2),  # Adding dropout for regularization
    tf.keras.layers.Dense(3, activation='linear',
                          kernel_regularizer=tf.keras.regularizers.l2(0.01),
                          kernel_initializer='he_normal')
])

# Compile the model using the custom loss function and custom learning rate
optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)  # Adjust the learning rate as needed
track_model.compile(optimizer=optimizer, loss=custom_loss, metrics=['mae'])
# Train the track model
# epochs: number of iterations over the entire training set
# batch_size: Number of samples used in each iteration for updating the models weights.
track_model.fit(X_train_tracks, y_train, epochs=250, batch_size=17, validation_data=(X_test_tracks, y_test))

# Initial Model: train all values
initial_model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],),
                          kernel_regularizer=tf.keras.regularizers.l2(0.01),
                          kernel_initializer='he_normal'),
    tf.keras.layers.Dense(64, activation='relu', name='hidden_layer_1',
                          kernel_regularizer=tf.keras.regularizers.l2(0.01),
                          kernel_initializer='he_normal'),
    tf.keras.layers.Dense(64, activation='relu', name='hidden_layer_2',
                          kernel_regularizer=tf.keras.regularizers.l2(0.01),
                          kernel_initializer='he_normal'),
    tf.keras.layers.Dropout(0.2),  # Adding dropout for regularization
    tf.keras.layers.Dense(3, activation='linear',
                          kernel_regularizer=tf.keras.regularizers.l2(0.01),
                          kernel_initializer='he_normal')
])

# Initial model Training phase
initial_optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)  # Adjust the learning rate as needed
initial_model.compile(optimizer=initial_optimizer, loss=custom_loss, metrics=['mae'], loss_weights=[1, 10, 1])
initial_model.fit(X_train, y_train, epochs=250, batch_size=17, validation_data=(X_test, y_test))

# combining the models
# Freeze the layers of the track_model
# meaning that it prevents the weights of those layers from being updated during training
for layer in track_model.layers:
    layer.trainable = False

# Create an input layer for the track features
input_tracks = Input(shape=(X_train_tracks.shape[1],))

# Create an input layer for all features
input_all = Input(shape=(X_train.shape[1],))

# Get the output from the track model
output_tracks = track_model(input_tracks)

# Get the output from the all features model
output_all = initial_model(input_all)

# Concatenate the outputs
merged = concatenate([output_tracks, output_all])

# Additional layers if needed
merged = Dense(128, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01),
               kernel_initializer='he_normal')(merged)
merged = Dropout(0.2)(merged)
merged_output = Dense(3, activation='linear')(merged)

# Create the combined model
combined_model = Model(inputs={'input_1': track_model.input, 'input_2': initial_model.input},
                       outputs=merged_output)

# Compile the combined model
optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)
combined_model.compile(optimizer=optimizer, loss=custom_loss, metrics=['mae'], loss_weights=[2, 5, 1])

# Train the combined model
combined_model.fit([X_train_tracks, X_train], y_train, epochs=250, batch_size=17,
                   validation_data=([X_test_tracks, X_test], y_test))

print(X_test_tracks.shape)

# Check predictions
y_pred = combined_model.predict({'input_1': X_test_tracks, 'input_2': X_test})
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

combined_model.save('models/modern_f1_era_quali_model.keras')

# Single value prediction
# first value is driver, second value is track, constructor is third
single_input = np.array([[64, 8, 28], [817, 71, 9]])
single_input_standardized = sc_X.transform(single_input)
predicted_output_standardized = combined_model.predict(single_input_standardized)
predicted_output = sc_y.inverse_transform(predicted_output_standardized)

# Print the predictions
print(X_test[[15]], X_test[[60]])
print("True values: \n", y_test[15], y_test[60])
predicted_output[predicted_output < 0] = 0
print(milliseconds_to_time_string([y_test[15]]), milliseconds_to_time_string([y_test[60]]))
print("Predictions : \n", predicted_output, "\n", milliseconds_to_time_string(predicted_output))
