# Importing the dataset
dataset = read.csv('50_Startups.csv')

# Encoding dummy values
dataset$State = factor(dataset$State,
                       levels = c("New York","Florida","California"),
                       labels = c(1,2,3))

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fitting Multiple linear regression to the Training set
# . means all the features
regressor = lm(formula = Profit ~ .,
               data = training_set)

# Predicting the test set results
y_pred = predict(regressor, newdata = test_set)

# Building optimal model using Backward Elimination (Remove valaues that have high P value (More than 5%))
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
               data = dataset)
summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
               data = dataset)
summary(regressor)

# P value 6%. Still need to remove Marketing. Not bad choice to leave it.
regressor = lm(formula = Profit ~ R.D.Spend + Marketing.Spend,
               data = dataset)
summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend,
               data = dataset)
summary(regressor)

# Prediction after Backward Elimination
y_pred = predict(regressor, newdata = test_set)
y_pred

# Backward Elimination automated
backwardElimination <- function(x, sl) {
  # X contains independent variables or features
  # SL signifigant lvl for variabel removal

  # Get the number of variables in dataset
    numVars = length(x)

    for (i in c(1:numVars)){
      # Fit the linear regression model (Profit is the dependent vector variable)
      regressor = lm(formula = Profit ~ ., data = x)

      # Get the largest P value from the summary
      maxVar = max(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"])

      # Check if the maxVar is larger than SL value (5%)
      if (maxVar > sl){
        # Get the index of the variable whit the largest P value
        j = which(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"] == maxVar)
        # Remove the variable whit the largest P value
        x = x[, -j]
      }
      # Update the number of variables after removal
      numVars = numVars - 1
    }
  # Return the new summary
    return(summary(regressor))
  }

# call the function whit the values
SL = 0.05
dataset = dataset[, c(1,2,3,4,5)]
backwardElimination(training_set, SL)