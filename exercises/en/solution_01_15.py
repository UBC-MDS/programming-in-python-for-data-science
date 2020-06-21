import pandas as pd

# The data

hockey_players = pd.read_csv('data/canucks.csv')

# Select the rows and columns 
# Save the new dataframe as penalty_players

penalty_players = hockey_players.loc[[10, 21, 2], ['Height', 'Weight', 'Salary', 'Country']]

# Display it

penalty_players
