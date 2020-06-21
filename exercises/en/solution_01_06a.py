import pandas as pd

# Read in the data

hockey_players = pd.read_csv('data/canucks.csv')

# Find the column names of hockey_players 
# Save it as columns_hockey

columns_hockey = hockey_players.columns

# Display it by writing the object name

columns_hockey
