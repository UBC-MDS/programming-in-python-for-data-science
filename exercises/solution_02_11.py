import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)

# Rename the column sp_attack to special_a and
# sp_defense to special_d using df.rename() once  
# Save the new dataframe as `pokemon_special`

pokemon_special = pokemon.rename(columns ={'sp_attack' : 'special_a',
                                           'sp_defense' : 'special_d'})

# Display the first 5 rows of the dataframe

pokemon_special.head()

