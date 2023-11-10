from sklearn.compose import ColumnTransformer
from sklearn.datasets import fetch_openml
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.svm import SVR
import pandas as pd
import numpy as np

# fetch dataset
adult = fetch_openml(name='adult', version=2)

# Combine features and target variable into a single DataFrame
df = pd.concat([pd.DataFrame(adult.data, columns=adult.feature_names), pd.Series(adult.target, name='target')], axis=1)

# Replace '?' with NaN and drop rows with missing values
df.replace('?', pd.NA, inplace=True)
df.dropna(inplace=True)

# Separate the features (X) and target variable (y) again
X = df.drop('target', axis=1)
y = df['target']

# Dummy variables... for countries to region...
# Yes chatGBT helped. No way I do this on my own
country_to_region = {
    'United-States': 'North America',
    'Cambodia': 'Asia',
    'England': 'Europe',
    'Puerto-Rico': 'North America',
    'Canada': 'North America',
    'Germany': 'Europe',
    'Outlying-US(Guam-USVI-etc)': 'North America',
    'India': 'Asia',
    'Japan': 'Asia',
    'Greece': 'Europe',
    'South': 'Other',
    'China': 'Asia',
    'Cuba': 'North America',
    'Iran': 'Asia',
    'Honduras': 'North America',
    'Philippines': 'Asia',
    'Italy': 'Europe',
    'Poland': 'Europe',
    'Jamaica': 'North America',
    'Vietnam': 'Asia',
    'Mexico': 'North America',
    'Portugal': 'Europe',
    'Ireland': 'Europe',
    'France': 'Europe',
    'Dominican-Republic': 'North America',
    'Laos': 'Asia',
    'Ecuador': 'South America',
    'Taiwan': 'Asia',
    'Haiti': 'North America',
    'Columbia': 'South America',
    'Hungary': 'Europe',
    'Guatemala': 'North America',
    'Nicaragua': 'North America',
    'Scotland': 'Europe',
    'Thailand': 'Asia',
    'Yugoslavia': 'Europe',
    'El-Salvador': 'North America',
    'Trinadad&Tobago': 'North America',
    'Peru': 'South America',
    'Hong': 'Asia',
    'Holand-Netherlands': 'Europe',
}

# If there is a country that is not listed in the array, it will be filled whit "Other" instead
X["region"] = X["native-country"].map(country_to_region).fillna("Other")
X = X.drop("native-country", axis=1)

print(X[["region"]])

# Encoding dummy values for X values
ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(sparse=False),
                                      ["region", "sex", "race", "relationship", "workclass", "education",
                                       "marital-status", "occupation"])],
                       remainder="passthrough")
X = np.array(ct.fit_transform(X))

# Label encoding for y values
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Splitting data to training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the SVR model on the Training set
regressor = SVR(kernel='rbf')
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = sc.inverse_transform(regressor.predict(sc.transform(X_test)).reshape(-1, 1))
# np.set_printoptions(precision=2)
# print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

# Evaluating the Model Performance
print("Predicted values:", y_pred)
print("True values:", y_test)
print(r2_score(y_test, y_pred))
