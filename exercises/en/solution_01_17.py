import pandas as pd

# The data

hockey_players = pd.read_csv('data/canucks.csv')

# Save Thatcher Demko's salary in an object named demko_paid

demko_paid = hockey_players.loc[4, 'Salary']
demko_paid

# How old is Zack MacEwen? Save it as object macewen_age

macewen_age = hockey_players.loc[10, 'Age']
macewen_age

# What position does Jacob Markstrom play? Save this as object markstrom_position

markstrom_position = hockey_players.loc[11, 'Position']
markstrom_position

# When was Justin Bailey born? Save it as an object named bailey_birth

bailey_birth = hockey_players.loc[0, 'Birth Date']
bailey_birth
