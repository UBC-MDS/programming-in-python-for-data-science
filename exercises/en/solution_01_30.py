import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv')

# Make an object named `position_column` that consists of just the `Position` column

position_column = hockey_players['Position']

# Find the frequencies of the position for the hockey team     
# Save it as `position_freq`

position_freq = position_column.value_counts()

# Export it to a csv named `position_frequencies.csv`

position_freq.to_csv('position_frequencies.csv')

# Don't forget to display it

position_freq
