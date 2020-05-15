import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv', index_col = 0)

# Sort the hockey_player dataframe by salary in descending order    
# Save it with the name "rich_players"   

rich_players = hockey_players.sort_values(by='Salary', ascending=False)

# Display it

rich_players



