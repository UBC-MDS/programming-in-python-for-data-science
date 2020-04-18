import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)

# Chain the following methods in the order specified
# Name the full chain pokemon_plot
# First, create a new column named AD_total by adding the attack and defense columns from the pokemon dataset
# Next drop the legendary column
# Use loc[] and slice from speed to AD_total
# Finally use .plot.scatter() to plot AD_total on the x-axis and capture_rt on the y-axis
# Use a new line for each method

pokemon_plot = (pokemon.assign(AD_total = pokemon['attack'] + pokemon['defense'])
                       .drop(columns = 'legendary')
                       .loc[: , 'speed': 'AD_total']
                       .plot.scatter(x = 'AD_total', y='capture_rt' )
)


