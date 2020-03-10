import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv')
hockey_players

# Slice the rows and columns and save the new dataframe as `benched_players`

benched_players = hockey_players.loc[ 7 : 19, "Player" : "Country"]

# Display it (without using print)

benched_players 