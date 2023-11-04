dataset = read.csv("Position_Salaries.csv")
dataset = dataset[2:3]

# Fitting linear regression to the dataset
# This no work sadge
lin_reg = lm(formula = Salary ~ Level,
             data = dataset)

# Fitting polynomial regression to the dataset
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
poly_reg = lm(formula = Salary ~ .,
              data = dataset)

library(ggplot2)
# Visualising Linear regression
ggplot()+
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = "red") +
  geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset)),
                colour = "blue") +
  ggtitle("Linear Regression") +
  xlab("Level") +
  ylab("Salary")

# Visualising Polynomial regression
ggplot()+
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = "red")+
  geom_line(aes(x = dataset$Level, y = predict(poly_reg,newdata = dataset)),
                colour = "blue") +
  ggtitle("Polynomial Regression") +
  xlab("Level") +
  ylab("Salary")

# Predicting new result whit linear regression
predict(lin_reg, newdata = data.frame(Level = 6.5))

# Predicting new result whit Polynomial regression
predict(poly_reg, newdata = data.frame(Level = 6.5,
                                       Level2 = 6.5^2,
                                       Level3 = 6.5^3,
                                       Level4 = 6.5^4))