import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv', index_col=0)
print(hockey_players)

# Slice the rows and columns and save the new dataframe as `benched_players`

benched_players = hockey_players.loc["Adam Gaudette": "Brandon Sutter", "No." : "Country"]

# Display it (without using print)

benched_players 