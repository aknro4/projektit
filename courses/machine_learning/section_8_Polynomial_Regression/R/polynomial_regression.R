dataset = read.csv("Position_Salaries.csv")
dataset = dataset[,2:3]

# Splitting data into test set and training set
#install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

lin_reg = lm(forumla = Salary ~ Level,
             data = dataset)


