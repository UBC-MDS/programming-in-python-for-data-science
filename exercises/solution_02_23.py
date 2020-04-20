import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)

# Slice the pokemon columns from attack to type 
# Save the new dataframe over object pokemon

pokemon = pokemon.loc[ : , 'attack': 'type']

# Make a groupby object on the column type and name it pokemon_type

pokemon_type = pokemon.groupby(by='type')

# Make a new dataframe named type_means using .mean() 
# containing the mean values of each pokemon type 

type_means = pokemon_type.mean() 
type_means

# Using .loc[] obtain from the type_means dataframe, the mean speed value of the 
# following pokemon types:
 
# fire and save it in an object named fire_mean_speed

fire_mean_speed = type_means.loc['fire', 'speed']
fire_mean_speed

# ice and save it in an object named ice_mean_speed

ice_mean_speed = type_means.loc['ice', 'speed']
ice_mean_speed

# water and save it in an object named water_mean_speed

ice_mean = type_means.loc['water', 'speed']
ice_mean
