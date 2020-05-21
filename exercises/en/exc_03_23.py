import pandas as pd

# We are going to import lego_top and lego_bottom which have 5001 rows and 6672 rows respectively.

lego_base = pd.read_csv('data/lego_theme_minimal.csv', index_col=0)
lego_opacity = pd.read_csv('data/lego_opacity.csv',  index_col=0)

# Combine the two dataframes horizontally to make 1 large complete dataframe using an outer join
# Name the new dataframe lego_full

____ = ____(____)

# make a new column named total_pieces by adding up columns matte and transparent
# Sort the dataframe by total_pieces in descending order
# Save this in an object named lego_details

# ____ = (____.____(____)
#            .____(____)
#       )

# Display the dataframe

# ____

