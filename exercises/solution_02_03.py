import pandas as pd

url = 'https://raw.githubusercontent.com/UBC-MDS/MCL-DSCI-511-programming-in-python/master/data/pokemon.csv'

# Read in the data from the URL using the pokemon name as the index

pokemon_df = pd.read_csv(url,index_col=0)

# Display the first 10 rows

pokemon_df.head(10)
