import pandas as pd

# Read in the data from the text file using the full pathway

pokemon_df = pd.read_csv('data/pokemon-text.txt', delimiter=";")

# Display the first 10 rows

pokemon_df.head(10)
