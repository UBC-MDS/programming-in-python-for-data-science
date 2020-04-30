import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)
pokemon = pokemon.loc[ : , 'attack': 'type']

# Make a groupby object on the column type and name it pokemon_type

# ____ = ____.____(____)

# Find the mean value of each column for each pokemon type using .mean() 
# and save the resulting dataframe as type_means

# ____ = ____.____()
# ____

# Obtain from the type_means dataframe, the mean speed of the
# water type pokemon by using df.loc[]
# # Save it in an object named water_mean_speed

# ____ = ____.____[____]

# Display it 

# ____
