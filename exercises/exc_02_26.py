import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)
pokemon = pokemon.loc[ : , 'attack': 'type']

# Make a groupby object on the column type 
# Find the mean value of each column for each pokemon type using .mean() 
# Save the resulting dataframe as type_means

# ____ = ____.____(____).____()
# ____

# Obtain the mean speed of each pokemon type from the dataframe 
# type_means by using .loc[]
# Save it in an object named mean_speed

# ____ = ____.____[____]

# Display it 

# ____
