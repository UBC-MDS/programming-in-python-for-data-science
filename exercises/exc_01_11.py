import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Loading in the data
candybar_df = pd.read_csv('data/candybars.csv', header=0, index_col=0)

print(candybar_df.head())

# Define X and y

X = candybar_df.drop(columns=['available_canada_america'])
y = candybar_df[['available_canada_america']]

# Creating a model

model = DecisionTreeClassifier()
print(model)

## Fit your data 
____.____

## Predict the labels of X
____.____

## The model accuracy
print("The accuracy of the model's prediction is " + "{:.1%}".format(model.score(X,y)))