import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)

# Create a new column named total_special 
# that is the sum of column sp_attack and sp_defense
# Save it as an object named pokemon_new_col

pokemon_new_col = pokemon.assign(total_special = pokemon['sp_attack'] + pokemon['sp_defense'])

# Drop the column deck_no from pokemon_new_col
# Save this dataframe as an object named pokemon_dropped

pokemon_dropped = pokemon_new_col.drop(columns='deck_no')

# Display the first 5 rows of the dataframe

pokemon_dropped.head()


