import pandas as pd

lego_sets = pd.read_csv('data/lego-sets.csv', index_col=0)
lego_inventory = pd.read_csv('data/inventory_sets.csv', index_col=0)

# Combine the two dataframes to make 1 large complete dataframe by using an outer join
# Make sure to set the argument indicator to True
# Name the new dataframe lego_tower

lego_stock = lego_inventory.merge(lego_sets, left_on='set_num', right_index=True, how='inner')

lego_stock

# At first glance it appears that we have 2846 different sets but let's check it thats right grouping by set_num and seeing how many groups are produced. 

lego_stock.groupby('set_num').ngroups

# Ah, it appears we have multiple rows for some of the same sets. How are we going to get the quantity of each set in stock?
# Let's continue this problem in the next section.
