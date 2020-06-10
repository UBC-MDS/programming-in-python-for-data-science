import pandas as pd

url = 'https://raw.githubusercontent.com/UBC-MDS/MCL-DSCI-511-programming-in-python/master/data/pokemon.csv'

# Read in the data from the URL 

pokemon_df = pd.read_csv(url)

# Display the first 10 rows

pokemon_df.head(10)
