import pandas as pd

lego = pd.read_csv('data/lego-sets.csv')
lego

# Create hierarchical indexes from the columns set_num and name
# Name the new dataframe lego_build

lego_build = lego.set_index(['set_num', 'name'])

# Display the dataframe

lego_build
