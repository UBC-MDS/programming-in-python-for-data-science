import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv', index_col=0)

# Select the rows and columns and save the new dataframe as `penalty_players`

penalty_players = hockey_players.loc[["Zack MacEwen", "Jake Virtanen", "Jordie Benn"], ["Height", "Weight", "Salary", "Country"]]

# Display it

penalty_players 
