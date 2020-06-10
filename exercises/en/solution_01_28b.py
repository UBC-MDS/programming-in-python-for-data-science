import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv')

# Find the total salary of the team and save it in an object called `player_cost`

player_cost = hockey_players[['Salary']].sum()

# Display it

player_cost


