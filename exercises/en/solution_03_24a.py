import pandas as pd

lego_sets = pd.read_csv('data/lego-sets.csv')
lego_inventory = pd.read_csv('data/inventory_sets.csv')

# Combine the two dataframes to make 1 large complete dataframe by using an inner join
# Name the new dataframe lego_stock

lego_stock = lego_inventory.merge(lego_sets,
                                  left_on='set_num', 
                                  right_on='set_num', 
                                  how='inner')
lego_stock

# At first glance it appears that we have 2846 different sets but
# let's check it thats right by grouping by set_num and seeing 
# how many groups are produced. 

lego_stock.groupby('set_num').ngroups


