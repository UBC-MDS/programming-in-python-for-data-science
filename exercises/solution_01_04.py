import pandas as pd

# Read in the dataset 

hockey_players = pd.read_csv('data/canucks.csv')

# Print the column names of `hockey_players` and save it as `columns_hockey`.

columns_hockey = hockey_players.columns 
columns_hockey

# Save the number of rows `hockey_players` has in a variable called `hockey_rows`.

hockey_rows = len(hockey_players)
hockey_rows

# Save the data frame shape as `hockey_shape`. 

hockey_shape = hockey_players.shape
hockey_shape
