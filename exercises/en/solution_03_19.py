import pandas as pd

# We are going to import lego_top and lego_bottom which have 5001 rows and 6672 rows respectively.

lego_top = pd.read_csv('data/lego_top.csv', index_col=0)
lego_bottom = pd.read_csv('data/lego_bottom.csv', index_col=0)

# Combine the two dataframes vertically to make 1 large complete dataframe
# Name the new dataframe full_set 

full_set  = pd.concat([lego_top, lego_bottom], axis=0)

# Save the new dimension of full_set in an object named full_set_shape

full_set_shape = full_set.shape

# Display the new dataframe

full_set


