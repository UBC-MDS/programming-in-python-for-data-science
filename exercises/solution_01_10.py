import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv', index_col=0)

# Slice the rows and columns and save the new dataframe as `star_players`

star_players = hockey_players.loc['Adam Gaudette': 'Brandon Sutter', 'No.' : 'Country']

# Display it

star_players 


