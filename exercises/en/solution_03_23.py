import pandas as pd

# We are going to import the dataframes lego_base and lego_opacity.

lego_base = pd.read_csv('data/lego_theme_minimal.csv', index_col=0)
lego_piece_type = pd.read_csv('data/lego_piece_type.csv',  index_col=0)

# Combine the two dataframes horizontally to make 1 large complete dataframe using an inner join
# Name the new dataframe lego_sets

lego_full = lego_base.merge(lego_opacity, )

# Make a new column named total_pieces by adding up columns matte and transparent
# Sort the dataframe by total_pieces in descending order
# Save this in an object named lego_details

lego_details = (lego_full.assign(total_pieces = lego_full['matte'] + lego_full['transparent'])
                                   .sort_values('total_pieces', ascending=False)
                       )

# Display the dataframe

lego_details

lego_piece_type

lego_base


