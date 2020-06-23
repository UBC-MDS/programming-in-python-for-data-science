import pandas as pd

# We are going to read in 2 new dataframes: lego_inventory_parts.csv and lego-colors.csv. 

lego_inventory = pd.read_csv('data/lego_inventory_parts.csv')
lego_colors = pd.read_csv('data/lego-colors.csv')

# Combine the two dataframes and name the new dataframe lego_tower

lego_tower = (lego_inventory.merge(lego_colors, 
                                  left_on='color_id', 
                                  right_on='id', 
                                  how='outer', 
                                  indicator=True)
             )
