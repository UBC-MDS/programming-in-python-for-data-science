import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)
pokemon = pokemon.loc[ : , 'attack': 'type']

# Make a groupby object on the column type and name it pokemon_type

pokemon_type = pokemon.groupby(by='type')

# Find the mean value of each column for each pokemon type using .mean() 
# and save the resulting dataframe as type_means

type_means = pokemon_type.mean() 
type_means

# Obtain from the type_means dataframe, the mean speed of the
# water type pokemon by using df.loc[]
# # Save it in an object named water_mean_speed

water_mean_speed = type_means.loc['water', 'speed']

# Display it 

water_mean_speed
