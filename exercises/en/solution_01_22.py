import pandas as pd

# The data

hockey_players = pd.read_csv('data/canucks.csv')

# Slice the rows and columns 
# Save the new dataframe as skilled_players

skilled_players = hockey_players.iloc[11:18, 0:4]

# Display it

skilled_players 
