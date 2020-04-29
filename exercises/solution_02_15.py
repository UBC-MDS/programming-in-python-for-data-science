import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)

# Create a new column named total_special 
# that is the sum of column sp_attack and sp_defense
# Save it, overwriting the dataframe named pokemon 

pokemon_new_col = pokemon.assign(total_special = pokemon['sp_attack'] + pokemon['sp_defense'])

# Display the first 5 rows of the dataframe

pokemon_dropped.head()


