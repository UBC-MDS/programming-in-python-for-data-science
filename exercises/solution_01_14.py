import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv')
print(hockey_players)

# Slice the rows and columns and save the new dataframe as `skilled_players`

skilled_players = hockey_players.iloc[11:18, 0:4]

# Display it (without using print)

skilled_players 