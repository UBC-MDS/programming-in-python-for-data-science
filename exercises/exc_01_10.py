import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv', index_col=0)
print(hockey_players)

# Select all the rows from column `Salary` only and save it as `player_cost` (Hint: you don't need `loc` here) 

____ = ____
print(____)

## Slice the rows and columns and save the new dataframe as `penalty_players`

____ = ____.____[____, ____]

# Display it (without using print)

____ 