import pandas as pd

# We are loading in  lego_stock from the last cell and the
# lego_sets dataframe

lego_stock = pd.read_csv('data/lego_stock.csv', index_col=0)
lego_sets = pd.read_csv('data/lego-sets.csv', index_col=0)

# Use groupby and agg to sum up the quantity of each set
# Save this as store_inventory 

store_inventory = (lego_stock.groupby('set_num')
                             .agg({'quantity':'sum'})
                  )

# We still want to know the set name, year, theme_id and number of parts that are 
# accessible from the lego_sets dataframe.
# We can get this back by inner joining store_inventory with lego_sets. 

# Use chaining to sort the dataframe in descending order based on in stock quantity
# Save this new dataframe as store_inventory_details 

store_inventory_details = (store_inventory.merge(lego_sets,
                                                 left_index=True,
                                                 right_index=True, 
                                                 how='inner')
                                          .sort_values('quantity', ascending=False)
                          )

# Display the full dataframe
store_inventory_details


