# Regression template

# Import data
dataset = read.csv("Position_Salaries.csv")
dataset = dataset[2:3]

# Fitting the Decision Tree regression model to the dataset
library(rpart)
regressor = rpart(formula = Salary ~ .,
                  data = dataset,
                  control = rpart.control(minsplit = 1))

# Predicting new result whit regression model
y_pred = predict(regressor, data.frame(Level = 6.5))

library(ggplot2)
# Visualising regression model
X_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot()+
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = "red")+
  geom_line(aes(x = X_grid, y = predict(regressor,data.frame(Level = X_grid))),
                colour = "blue") +
  ggtitle("Decision Tree regression model") +
  xlab("Level") +
  ylab("Salary")


