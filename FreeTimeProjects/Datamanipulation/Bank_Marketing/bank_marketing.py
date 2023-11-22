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

# fetch dataset
# https://archive.ics.uci.edu/dataset/222/bank+marketing
bank_marketing = fetch_ucirepo(id=222)

# data (as pandas dataframes)
X = bank_marketing.data.features
y = bank_marketing.data.targets

# Noted to be not needed and should be removed, thinking about removing month
drop = ["duration", "day_of_week", "contact"]
X = X.drop(drop, axis=1)

# filtering and editing whole dataset
# Convert features and targets to Pandas DataFrames
X_df = pd.DataFrame(X, columns=bank_marketing.feature_names)  # Assuming 'feature_names' exist in bank_marketing
y_df = pd.DataFrame(y, columns=bank_marketing.targets_names)  # Replace 'target' with appropriate column name

# Combine X and y into a single DataFrame
combined_df = pd.concat([X_df, y_df], axis=1)

# Job.
# 3 categories: retired, unemployed, working.
# Remove unknown ones
working = ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'self-employed', 'services',
           'technician']
unemployed = ["unemployed", "student"]
combined_df["job"].replace(working, "working", inplace=True)
combined_df["job"].replace(unemployed, "unemployed", inplace=True)
combined_df["job"].replace("unknown", np.nan, inplace=True)
combined_df = combined_df.dropna(subset=['job'])

# marital
# Single or married and once again remove unknown ones
single = ["divorced", "single"]
combined_df["marital"].replace(single, "single", inplace=True)
combined_df["marital"].replace("unknown", np.nan, inplace=True)
combined_df = combined_df.dropna(subset=['marital'])

# Education
# 'basic.4y','basic.6y','basic.9y' all these to same category basic.
# Remove unknown once's
basic = ['basic.4y', 'basic.6y', 'basic.9y']
combined_df["education"].replace(basic, "basic", inplace=True)
combined_df["education"].replace("unknown", np.nan, inplace=True)
combined_df = combined_df.dropna(subset=['education'])

# Poutcome
# Just remove nan values and nonexistent
combined_df["poutcome"].replace("nonexistent", np.nan, inplace=True)
combined_df = combined_df.dropna(subset=['poutcome'])

# Age
# Instead of exact age. We should but them into age groups
# Teen:18-25, Young_adult:26-35, adult:36-50, senior:51-65,	retired:66+
# BUT. this does affect the accuracy of the model.
# And also means that when doing single prediction, the value has to be categorized
# Define conditions for each age group
conditions = [
    (combined_df['age'].between(18, 25)),
    (combined_df['age'].between(26, 35)),
    (combined_df['age'].between(36, 50)),
    (combined_df['age'].between(51, 65)),
    (combined_df['age'] >= 66)
]

# Define corresponding labels for each condition
labels = ['teen', 'young_adult', 'adult', 'senior', 'retired']

# Apply conditions and assign labels
combined_df['age'] = np.select(conditions, labels, default='Unknown')

# Pdays
# Found that some pdays values go over 800 so decided to do few more groups than originally (4 groups)
# Groups. I mean you can see the groups below.
# BUT. this does affect the accuracy of the model.
# Define conditions for each pdays group
conditions = [
    (combined_df['pdays'] == -1),
    (combined_df['pdays'].between(0, 90)),
    (combined_df['pdays'].between(91, 180)),
    (combined_df['pdays'].between(181, 270)),
    (combined_df['pdays'].between(271, 365)),
    (combined_df['pdays'].between(366, 730)),
    (combined_df['pdays'] >= 731)
]

# Define corresponding labels for each condition
labels = [
    'no_contact',
    'within_3_months',
    'within_3_to_6_months',
    'within_6_to_9_months',
    'within_9_to_12_months',
    'within_second_year',
    'within_third_year_and_over'
]

# Apply conditions and assign labels
combined_df['pdays'] = np.select(conditions, labels, default='Unknown')

# Balance average yearly balance
# Adding groups Data provided is difficult.
# persons making <=25000 count is 7800 ish so almost whole dataset
# So making groups whit 5k difference up to 30k
conditions = [
    (combined_df['balance'] < 0),
    (combined_df['balance'].between(0, 5000)),
    (combined_df['balance'].between(5001, 10000)),
    (combined_df['balance'].between(10001, 15000)),
    (combined_df['balance'].between(15001, 20000)),
    (combined_df['balance'].between(20001, 25000)),
    (combined_df['balance'].between(25001, 30000)),
    (combined_df['balance'] >= 30001)
]

# Define corresponding labels for each condition
labels = [
    'negative_balance',
    '0-5k_balance',
    '5k-10k_balance',
    '10k-15k_balance',
    '15k-20k_balance',
    '20k-25k_balance',
    '25k-30k_balance',
    'over-30k_balance',
]

# Apply conditions and assign labels
combined_df['balance'] = np.select(conditions, labels, default='Unknown')


# Filtering proces result
# from 45211 x 16
# to [7907 rows x 43 columns]

to_CSV = combined_df
to_CSV.to_csv("training_data/whole_dataset.csv", index=False)

# Separate combined back to original
X = combined_df.iloc[:, :-1]
y = combined_df.iloc[:, -1:]

# Dealing whit empty values
# X.replace(np.NaN,"")
to_CSV = X
to_CSV.to_csv("training_data/training_data.csv", index=False)
y_to_CSV = y
y_to_CSV.to_csv("training_data/y_data.csv", index=False)

# Label encodeer
label_encoder = LabelEncoder()

# Label encoding y values, Should be fine... Right? Just yes or no... Right?
y = label_encoder.fit_transform(y.astype(str))

# OneHotEncoding or dealing whit dummy dum dum values
categorical_columns = ["job", "marital", "education", "default", "housing", "loan", "month",
                       "poutcome", "age", "pdays"]
numerical_values = ["balance", "campaign", "previous"]

ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), categorical_columns)], remainder="passthrough")

# Apply the transformation to the dataset
X_transformed = ct.fit_transform(X)

# Get feature names after transformation
# some reason I'm little-bit scared about this
if hasattr(ct.named_transformers_['encoder'], 'get_feature_names_out'):
    transformed_columns = ct.named_transformers_['encoder'].get_feature_names_out(input_features=categorical_columns)
else:
    transformed_columns = ct.named_transformers_['encoder'].get_feature_names(categorical_columns)

# Combine with numerical column names
transformed_columns = list(transformed_columns) + numerical_values
X = pd.DataFrame(X_transformed, columns=transformed_columns)
X_to_CSV = X
X_to_CSV.to_csv("training_data/X_data.csv", index=False)

print(X)
# Splitting the data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Define the parameter grid for RCF, for cleaner code sake
param_grid = {
    'n_estimators': [100, 300, 500],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 3, 5],
    'min_samples_leaf': [1, 2],
}


# Previously used RCF whit gridsearch.
# Did not getter better result than a SINGLE Xgboost
# So we are using that instead

# Xgboot
print("XGB turn... never used this before")
start_time = time.time()
# readable format
time_object_start = datetime.fromtimestamp(start_time)
formatted_date = time_object_start.strftime('%H:%M:%S')
print(formatted_date)

# Define the parameter grid for XGB

param_grid_xgb = {
    'learning_rate': [0.01, 0.1, 0.2],
    'n_estimators': [15, 45, 75], # Decrees these later
    'max_depth': [3, 5, 7],
    'subsample': [0.7, 0.8, 0.9],
    'colsample_bytree': [0.7, 0.8, 0.9],
    'reg_alpha': [0, 0.1, 1],
    'reg_lambda': [0, 1, 10],
    'device': ["cuda", "cuda", "cuda"],
    'tree_method': ["hist", "hist", "hist"]
}
# Initialize GridSearchCV for XGBClassifier
grid_search_xgb = GridSearchCV(xgb.XGBClassifier(objective='binary:logistic', eval_metric='error'),
                               param_grid_xgb, cv=5, scoring='accuracy', n_jobs=1)

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
