import pandas as pd

# Read in the dataset 

hockey_players = pd.read_csv('data/canucks.csv', index_col=0)

# Find the column names of `hockey_players` save it as `columns_hockey` 

columns_hockey = hockey_players.columns 

# Display it by writing the object name.

columns_hockey 



