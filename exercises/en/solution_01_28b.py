import pandas as pd

# The data

hockey_players = pd.read_csv('data/canucks.csv')

# Find the total salary of the team 
# Save it in an object called player_cost

player_cost = hockey_players[['Salary']].sum()

# Display it

player_cost


