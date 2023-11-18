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

# Noted to be not needed and should be removed
X = X.drop("duration", axis=1)
X = X.drop("day_of_week", axis=1)
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
categorical_columns = ["job", "marital", "education", "default", "housing", "loan", "contact", "month",
                       "poutcome"]
numerical_values = ["age", "balance", "campaign", "pdays", "previous"]

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


# Splitting the data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Define the parameter grid for RCF, for cleaner code sake
param_grid = {
    'n_estimators': [100, 500, 1000],
    'max_depth': [None, 5, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
}

# Initialize GridSearchCV
grid_search = GridSearchCV(RandomForestClassifier(random_state=0), param_grid, cv=5, scoring='accuracy',
                           error_score='raise')

# Start tracking time
print("Training in process and time started")
start_time = time.time()
print(start_time)

# Train model
grid_search.fit(X_train, y_train)
# Get the best parameters
best_params = grid_search.best_params_
best_estimator = grid_search.best_estimator_
# Train the model using the best parameters
best_estimator.fit(X_train, y_train)

# Calculate training duration
end_time = time.time()
train_duration = end_time - start_time
print("Training time: ", train_duration)


# RCF predictions
y_pred_rcf = best_estimator.predict(X_test)
print("R2 score", r2_score(y_test, y_pred_rcf))
# And validation
accuracy = accuracy_score(y_test, y_pred_rcf)
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred_rcf))

# Features importance
importance = best_estimator.feature_importances_
print("Feature importance: ", importance)

# Dump or save the model
dump(best_estimator, "models/bank_marketing.joblib")


# Xgboot
print("XGB turn... never used this before")
xgb_classifier = xgb.XGBClassifier(
    learning_rate=0.1,
    n_estimators=100,
    max_depth=5,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=0.1,
    reg_lambda=1,
    objective='binary:logistic',  # For binary classification
    eval_metric='error'  # Evaluation metric
)
xgb_classifier.fit(X_test, y_test)

# XGB predictions
print("Feature importance: ", xgb_classifier.get_booster().get_score(importance_type='weight'))
y_pred_xgb = xgb_classifier.predict(X_test)
print("R2 score", r2_score(y_test, y_pred_xgb))
# And validation
accuracy = accuracy_score(y_test, y_pred_xgb)
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred_xgb))
