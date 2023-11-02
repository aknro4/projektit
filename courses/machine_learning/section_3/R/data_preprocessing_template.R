dataset = read.csv("Data.csv")
# dataset = dataset[,2:3]

# Splitting data into test set and training set
#install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature scaling 
# training_set[, 2:3] = scale(training_set[,2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])
