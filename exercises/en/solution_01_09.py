import pandas as pd

# The database

hockey_players = pd.read_csv('data/canucks.csv')

# Slice the rows and columns and save the new dataframe as `benched_players`

benched_players = hockey_players.loc[3:9]

# Display it

benched_players
