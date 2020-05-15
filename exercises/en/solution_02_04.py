import pandas as pd

# Read in the data from the text file using the full pathway
# Use the pokemon name as the index

pokemon_df = pd.read_csv('data/pokemon-text.txt',
                         index_col=0, 
                         delimiter=";")

# Display the first 10 rows

pokemon_df.head(10)
