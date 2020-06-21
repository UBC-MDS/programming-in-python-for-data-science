import pandas as pd

# Read in the data

hockey_players = pd.read_csv('data/canucks.csv')

# Find the the data frame shape of hockey_players 
# Save it as  as hockey_shape

hockey_shape = hockey_players.shape

# Display it by writing the object name

hockey_shape
