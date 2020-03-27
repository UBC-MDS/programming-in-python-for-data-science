import pandas as pd

# Read in the dataset 

hockey_players = pd.read_csv('data/canucks.csv', index_col=0)

# Find the the data frame shape of `hockey_players` save it as  as `hockey_shape' 

hockey_shape = hockey_players.shape

# Display it by writing the object name.

hockey_shape
