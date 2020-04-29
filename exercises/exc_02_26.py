import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)
pokemon = pokemon.loc[ : , 'attack': 'type']

# Make a groupby object on the column type and name it pokemon_type

# ____ = ____.____(____)

# Find the mean value of each column for each pokemon type using .mean() 
# and save the resulting dataframe as type_means

# ____ = ____.____()
# ____

# Obtain from the type_means dataframe, the mean speed of the following 
# pokemon types by using df.loc[]:

# fire and save it in an object named fire_mean_speed

# ____ = ____.____[____]
# ____

# ice and save it in an object named ice_mean_speed

# ____ = ____.____[____]
# ____

# water and save it in an object named water_mean_speed

# ____ = ____.____[____]
# ____
