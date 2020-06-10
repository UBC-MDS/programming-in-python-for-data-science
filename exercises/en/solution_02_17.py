import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv')

# Create a new dataframe named fire_pokemon containing only the rows of type "fire" 

fire_pokemon = pokemon[pokemon['type'] == 'fire']

