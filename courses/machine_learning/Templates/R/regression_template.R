# Regression template

# Import data
dataset = read.csv("data.csv")
# dataset = dataset[2:3]

# Fitting the regression model to the dataset
# create regressor

# Predicting new result whit regression model
y_pred = predict(regressor, newdata = data.frame(feature = predict))

library(ggplot2)
# Visualising regression model
ggplot()+
  geom_point(aes(x = dataset$X, y = dataset$Y),
             colour = "red")+
  geom_line(aes(x = dataset$Level, y = predict(regressor,newdata = dataset)),
                colour = "blue") +
  ggtitle("Regression regression model") +
  xlab("X label") +
  ylab("Y label")


