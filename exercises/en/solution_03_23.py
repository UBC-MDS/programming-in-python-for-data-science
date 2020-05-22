import pandas as pd

# We are going to read in 2 new dataframes: lego_inventory_parts.csv and lego-colors.csv. 

lego_inventory = pd.read_csv('data/lego_inventory_parts.csv', index_col=0)
lego_colors = pd.read_csv('data/lego-colors.csv', index_col=0)

# Combine the two dataframes to make 1 large complete dataframe by using an outer join
# Make sure to set the argument indicator to True
# Name the new dataframe lego_tower

lego_tower = lego_inventory.merge(lego_colors, left_on='color_id', right_index=True,  how='outer', indicator=True)
