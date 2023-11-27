import os
from datetime import datetime
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.svm import SVC
from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
import xgboost as xgb
import time
from joblib import dump, load
from EditingData import FilteringData


# Check if there is a file called whole_dataset
if os.path.isfile("training_data/whole_dataset.csv") is False:
    # If not create it
    FilteringData()

dataset = pd.read_csv("training_data/whole_dataset.csv")


# Separate dataset
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1:]

# Make CSV files.
to_CSV = X
to_CSV.to_csv("training_data/X_data.csv", index=False)
y_to_CSV = y
y_to_CSV.to_csv("training_data/y_data.csv", index=False)

# Label encoder
label_encoder = LabelEncoder()

# Label encoding y values, Should be fine... Right? Just yes or no... Right?
y = label_encoder.fit_transform(y.astype(str))

# OneHotEncoding or dealing whit dummy dum dum values
categorical_columns = ["job", "marital", "education", "default", "housing", "loan", "month",
                       "poutcome", "age", "pdays", "balance","campaign", "previous"]

ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), categorical_columns)], remainder="passthrough")

# Apply the transformation to the dataset
X = ct.fit_transform(X)

# Splitting the data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# For excel
X_test_TO_CSV = X_test
X_test_TO_CSV.to_CSV.to_csv("training_data/X_test_data.csv", index=False)
y_test_TO_CSV = y_test
y_test_TO_CSV.to_CSV.to_csv("training_data/y_test_data.csv", index=False)


# Thinking about making each model their own class to clear up the code

# Start training time for RCF
start_time = time.time()
# readable format
time_object_start = datetime.fromtimestamp(start_time)
formatted_date = time_object_start.strftime('RCF Timer: '+'%H:%M:%S')
print(formatted_date)

# RCF Param
param_grid_RCF = {
    'n_estimators': [50, 100, 200],  # Number of trees in the forest
    'max_depth': [None, 10, 20],  # Maximum depth of the trees
    'min_samples_split': [2, 5, 10],  # Minimum samples required to split a node
    'min_samples_leaf': [1, 2, 4],  # Minimum samples required at each leaf node
    'max_features': ['sqrt', 'log2'],  # Number of features to consider for best split
    'bootstrap': [True, False]  # Whether bootstrap samples are used when building trees
}

# Random Forest Classifier
rf_classifier = RandomForestClassifier(random_state=0)

# Create GridSearchCV
grid_search_RCF = GridSearchCV(estimator=rf_classifier, param_grid=param_grid_RCF, cv=5, n_jobs=-1, verbose=2)

# Fit the model to the data
grid_search_RCF.fit(X_train, y_train)

# Get the best parameters and the best score
best_params_RCF = grid_search_RCF.best_params_
best_score_RCF = grid_search_RCF.best_score_

# Calculate training duration
end_time = time.time()
train_duration = end_time - start_time
time_object_start = datetime.fromtimestamp(train_duration)
formatted_date = time_object_start.strftime('%H:%M:%S')
print("Training time: ", formatted_date)

# RCF predictions
y_pred_RCF = best_score_RCF.predict(X_test)
print("R2 score", r2_score(y_test, y_pred_RCF))
# And validation
accuracy = accuracy_score(y_test, y_pred_RCF)
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred_RCF))

# Feature importance
# Access feature importances
feature_importances = best_score_RCF.feature_importances_
# Match feature importances with column names
feature_importance_dict = dict(zip(X.columns, feature_importances))
# Sort feature importances by their values
sorted_feature_importances = sorted(feature_importance_dict.items(), key=lambda x: x[1], reverse=True)

# Display the feature importances
for feature, importance in sorted_feature_importances:
    print(f"Feature: {feature}, Importance: {importance}")

# Dump or save the model
dump(best_score_RCF, "models/bank_marketing_RCF.joblib")


# Xgboot
print("XGB turn... never used this before")
start_time = time.time()
# readable format
time_object_start = datetime.fromtimestamp(start_time)
formatted_date = time_object_start.strftime('%H:%M:%S')
print(formatted_date)

# Define the parameter for XGB.
# Cant train. cpu overheats, and gpu training does not get triggered some reason
param_grid_xgb = {
    'learning_rate': [0.01, 0.1, 0.2],
    'n_estimators': [15, 45, 75],  # Decrees these later
    'max_depth': [3, 5, 7],
    'subsample': [0.7, 0.8, 0.9],
    'colsample_bytree': [0.7, 0.8, 0.9],
    'reg_alpha': [0, 0.1, 1],
    'reg_lambda': [0, 1, 10],
#    'device': ["cuda", "cuda", "cuda"],
#    'tree_method': ["hist", "hist", "hist"]
}
# Initialize GridSearchCV for XGBClassifier
grid_search_xgb = GridSearchCV(xgb.XGBClassifier(objective='binary:logistic', eval_metric='error'),
                               param_grid_xgb, cv=5, scoring='accuracy', n_jobs=-1)

# Fit the grid search
grid_search_xgb.fit(X_train, y_train)

# Get the best parameters and best estimator
best_params_xgb = grid_search_xgb.best_params_
best_estimator_xgb = grid_search_xgb.best_estimator_

# Calculate training duration
end_time = time.time()
train_duration = end_time - start_time
time_object_start = datetime.fromtimestamp(train_duration)
formatted_date = time_object_start.strftime('%H:%M:%S')
print("Training time: ", formatted_date)

# XGB predictions
print("Feature importance: ", best_estimator_xgb.get_booster().get_score(importance_type='weight'))
y_pred_xgb = best_estimator_xgb.predict(X_test)
print("R2 score", r2_score(y_test, y_pred_xgb))
# And validation
accuracy = accuracy_score(y_test, y_pred_xgb)
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred_xgb))

# Dump or save the model
dump(best_estimator_xgb, "models/bank_marketing_XGB.joblib")
