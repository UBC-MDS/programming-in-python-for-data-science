import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv', index_col=0)

# Slice the rows and columns and save the new dataframe as `benched_players`

benched_players = hockey_players.loc["Justin Bailey": "Tim Schaller", "Age" : "Country"]

# Display it

benched_players 