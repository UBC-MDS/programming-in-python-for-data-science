import pandas as pd

# We loading in our previous combined dataframe lego_stock and our previous lego_sets dataframe 

lego_stock = pd.read_csv('data/lego_stock.csv', index_col=0)
lego_sets = pd.read_csv('data/lego-sets.csv', index_col=0)

# Use groupby and agg to sum up the quantity of each set. 
# Save this as store_inventory 

store_inventory = lego_stock.groupby('set_num').agg({'quantity': 'sum'})

# We still want to know the set name, year, theme_id and number of parts that were accessible from the lego_sets dataframe. We can get this back by inner joining store_inventory with lego_sets. Save this new dataframe as store_inventory_details 

store_inventory_details = store_inventory.merge(lego_sets, left_index=True, right_index=True, how='inner')

store_inventory_details


