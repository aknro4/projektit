import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# Whit other Classifier models we don't need to remove the id colum,
# cause the models will recolonize it does not affect the result
dataset = pd.read_csv("breast_cancer.csv")
# But for this model we need to manually remove the first value. Other vise all predictions will be 2
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Splitting teh data into training set and the test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Training the logistic regression model on the Training set
classifier = LogisticRegression(random_state=0).fit(X_train, y_train)

# Predicting Test set values
y_pred = classifier.predict(X_test)
print("Predicting results \n", y_pred, "\n Reals or 'Correct' values \n", y_test)

# Confusion metrix and accuracy score.
cm = confusion_matrix(y_test, y_pred)
print("Confusion metrix \n", cm, "\n Accuracy score \n", accuracy_score(y_test, y_pred) * 100)

# Confusion matrix output
# [[103   4] 103(2) and 59(4) are correct predictions. 4 and 5 are incorrect predictions
# [  5  59]] so from 59 predictions model got 4 wrong.

# Computing accuracy whit K-Fold cross validation
accuracies = cross_val_score(estimator=classifier, X=X_train, y=y_train, cv=10)
print("Accuracies average: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))
