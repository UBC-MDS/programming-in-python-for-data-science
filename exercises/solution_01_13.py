import sys
sys.path.insert(0, 'exercises/')

from gini_impurity import gini2

import numpy as np
import pandas as pd

# Loading in the data
candybar_df = pd.read_csv('data/candybars.csv', header=0, index_col=0)

# Wranging the data so we only have 2 categories
candybar_df = candybar_df[candybar_df['available_canada_america']!= "Both"]

# Looking at just peanuts and the class of each
candybar_df_con = candybar_df[['peanuts','available_canada_america']]
print(candybar_df_con)

# Finding the counts of each label for porportions - This will be helpful.  
print(candybar_df['available_canada_america'].value_counts())

# How many observations are there in total? 
obs_total = 16

# How many observations have peanuts >= 0.5? 
obs_peanuts = 6

# Of those observations how many are classed as America and Canada? 
peanut_america = 5
peanut_canada = 1

# How many observations have peanuts < 0.5? 
obs_not_peanuts = 10

# Of those observations how many are classed as America and Canada? 
not_peanut_america = 3
not_peanut_canada = 7

# Insert the correct values into the equation.
peanut_gini_impurity = gini2(5, 1)*(6/16) + gini2(3, 7)*(10/16)
print(peanut_gini_impurity)