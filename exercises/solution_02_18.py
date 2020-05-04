import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)

# Filter the dataframe for the pokemon that have attack and
# defense values both greater than 100
# Save this dataframe as an object named mighty_pokemon

mighty_pokemon = pokemon[(pokemon['defense'] > 100) & (pokemon['attack'] > 100)]

