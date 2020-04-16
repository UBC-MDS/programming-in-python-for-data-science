import pandas as pd

# Read in the data from the text file using the pokemon name as the index

pokeman_df = pd.read_excel('data/pokemon.xlsx', index_col=0, sheet_name="pokemons")

# Display  the first 10 rows

pokeman_df.head()
