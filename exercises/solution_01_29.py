import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv', index_col = 0)

# Make an object named `position_column` that consists of just the `Position` column.      
# Note we will be using this for `value_counts` so we must do this with only using single `[]` brackets. 

position_column = hockey_players["Position"]

# Find the frequencies of the position for the hockey team using `df.value_counts()`.      
# Save it as `position_freq`. 

position_freq = position_column.value_counts()

# Export it to a csv named `position_frequencies.csv` using `pd.to_csv()`.

position_freq.to_csv("position_frequencies.csv")

# Don't forget to display it

position_freq
