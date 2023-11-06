# SVR Regression model

# Import data
dataset = read.csv("Position_Salaries.csv")
dataset = dataset[2:3]

# Fitting the SVR regression model to the dataset
library(e1071)
regressor = svm(formula = Salary ~ .,
                data = dataset,
                type = "eps-regression")

# Predicting new result whit SVR regression model
y_pred = predict(regressor, newdata = data.frame(Level = 6.5))

library(ggplot2)
# Visualising SVR regression model
ggplot()+
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = "red")+
  geom_line(aes(x = dataset$Level, y = predict(regressor,newdata = dataset)),
                colour = "blue") +
  ggtitle("SVR Regression model") +
  xlab("X label") +
  ylab("Y label")


