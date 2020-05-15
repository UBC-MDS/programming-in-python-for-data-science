import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv', index_col = 0)

# Find the statistics of both categorical and quantitive columns.   
# Save the dataframe in an object called `hockey_stats`

hockey_stats = hockey_players.describe(include = 'all')

# Display it

hockey_stats
