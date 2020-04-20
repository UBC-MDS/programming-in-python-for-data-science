import pandas as pd

# Read in the data from the URL using the pokemon name as the index

pokemon_df = pd.read_csv('https://raw.githubusercontent.com/UBC-MDS/MCL-DSCI-511-programming-in-python/master/data/pokemon.csv',
                          index_col=0)

# Display the first 10 rows

pokemon_df.head(10)
