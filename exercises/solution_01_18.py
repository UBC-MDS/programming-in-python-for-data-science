import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv', index_col = 0)

# Find the statistics of both categorical and quantitive columns. 
# Save the dataframe in an object called `hockey_stats`

hockey_stats = hockey_players.describe(include = "all")
hockey_stats

# Save the most prominent country in an object called `hockey_country` (_Don't forget to put it between "quotation"_)

hockey_country = "Canada"
hockey_country

# Save the value of the tallest play in `tallest_height`

tallest_height = 203
tallest_height

# What is the youngest age? Save it in an object named `youngest_age`

youngest_age = 20
youngest_age


# Find the total Salary of the team and save it in an object called `player_cost`

player_cost = hockey_players[["Salary"]].sum()
player_cost
