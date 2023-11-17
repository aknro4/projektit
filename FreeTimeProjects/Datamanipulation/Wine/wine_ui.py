import tkinter as tk

import matplotlib
import matplotlib.pyplot as plt
from joblib import dump, load
import numpy as np
import pandas as pd
import random

# Loading the model
predict_wine = load("model/RFC_Wine.joblib")

# Load training data for random values
dataset = pd.read_csv("training_data/X_wine.csv")


# Columns that are needed to make prediction
columns = ["Alcohol", "Malicacid", "Ash", "Alcalinity_of_ash", "Magnesium", "Total_phenols",
           "Flavanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue",
           "0D280_0D315_of_diluted_wines", "Proline"]


# Function to plot the graph
def predict_and_visualize():
    try:
        # Our index tracker, guess index would be better name
        counter = 0
        input_values = [[]]

        # Sets random values based on X datas min max values to predict
        # if any of the input values are empty.
        random_values = [[]]
        for column_random in dataset.columns:
            min_val = dataset[column_random].min()
            max_val = dataset[column_random].max()
            random_values[0].append(round(random.uniform(min_val, max_val), 3))

        for column_insert in columns:
            # Check if entry is empty if not use the inputted value instead
            if len(entry_fields[column_insert].get()) == 0:
                input_values[0].append(float(random_values[0][counter]))
            else:
                input_values[0].append(float(entry_fields[column_insert].get()))
            counter += 1

        # Format the data to DataFrame
        df = pd.DataFrame(input_values, columns=columns)

        # Making prediction using wine model
        prediction = predict_wine.predict_proba(df)

        # Visualization - Creating a bar chart
        classes = ['Class 1', 'Class 2', 'Class 3']  # Replace with your actual class labels
        plt.figure(figsize=(9, 6))
        plt.bar(classes, prediction[0], color=['red', 'green', 'blue'])
        plt.title('Wine Class Prediction Probabilities')
        # Show only values used to predict
        df_string = ', '.join(map(str, input_values[0]))
        # print(df_string)
        plt.xlabel('Wine Classes And values used to predict\n'
                   + df_string)
        plt.ylabel('Predicted Probabilities')
        plt.ylim(0, 1) # Set y-axis limit from 0 to 1 for probabilities
        plt.show()

    except Exception as e:
        tk.messagebox.showerror("Error", str(e))


# Create the main Tkinter window
root = tk.Tk()
root.title("Wine Prediction")


# Displaying text some text
label_text = ("You can leave the values empty if you want to predict random values. \n"
              "Or enter some own values and leave some values empty.")
label = tk.Label(root, text=label_text)
label.pack()

# Dictionary to store Entry fields
entry_fields = {}

# Create input fields for each column
for column in columns:
    label_text = f"Enter {column.replace('_', ' ')} Value:"  # Format label text
    label = tk.Label(root, text=label_text)
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    entry_fields[column] = entry  # Store Entry field in the dictionary

# Button to trigger plot generation
plot_button = tk.Button(root, text="Predict", command=predict_and_visualize)
plot_button.pack()

# Start the main event loop
root.mainloop()
