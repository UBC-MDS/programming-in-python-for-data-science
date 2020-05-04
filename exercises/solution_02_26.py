import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)
pokemon = pokemon.loc[ : , 'attack': 'type']

# Make a groupby object on the column type 
# Find the mean value of each column for each pokemon type using .mean() 
# Save the resulting dataframe as type_means

type_means = pokemon.groupby(by='type').mean() 
type_means

# Obtain from the type_means dataframe, the mean speed of the
# water type pokemon by using df.loc[]
# Save it in an object named water_mean_speed

water_mean_speed = type_means.loc['water', 'speed']

# Display it 

water_mean_speed
