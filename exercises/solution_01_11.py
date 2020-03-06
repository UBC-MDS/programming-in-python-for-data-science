import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv')
print(hockey_players)

# Select all the rows from column `Age` only and save it as `player_ages` (Hint: you don't need `loc` here) 

player_ages = hockey_players[["Age"]]
print(player_ages)

## Slice the rows and columns and save the new dataframe as `penalty_players`

penalty_players = penalty_players = hockey_players.loc[[10, 21, 2], ["Player", "Height", "Weight", "Salary", "Country"]]

# Display it (without using print)

penalty_players 