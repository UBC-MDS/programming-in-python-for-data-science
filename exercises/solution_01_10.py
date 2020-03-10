import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv', index_col=0)
hockey_players

# Select all the rows from column `Salary` only and save it as `player_cost` (Hint: you don't need `loc` here) 

player_cost = hockey_players[["Salary"]]
player_cost

## Slice the rows and columns and save the new dataframe as `penalty_players`

penalty_players = hockey_players.loc[["Zack MacEwen", "Jake Virtanen", "Jordie Benn"], ["Height", "Weight", "Salary", "Country"]]

# Display it (without using print)

penalty_players 