import pandas as pd
pokemon = pd.read_csv('data/pokemon.csv')

# Create a new column in the dataframe Name the column base_score, 
# by assigning values 500 or greater from the column total_bs
# as 'strong' pokemon and values less than 500 as 'weak' pokemon

pokemon.loc[pokemon['total_bs'] >= 500, 'base_score']  = 'strong'
pokemon.loc[pokemon['total_bs'] < 500, 'base_score']  = 'weak'

# Display the first 10 rows of the dataframe

pokemon.head(10)
