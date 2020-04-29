import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)

# Filter the dataframe for the pokemon that have 
# either a total base score "total_bs" greater than 650 or a speed greater than 140
# All the pokeman must be legendary as well(= 1) 
# Save this dataframe as an object named legendary_pokemon

legendary_pokemon = pokemon[((pokemon['total_bs'] > 650) | 
                             (pokemon['speed'] > 140)) & 
                             (pokemon['legendary'] == 1)]

# Display the first 10 rows of the dataframe

legendary_pokemon.head(10)

