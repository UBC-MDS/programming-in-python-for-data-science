import pandas as pd

# Read in the data from the Excel file using the full pathway
# Use the pokemon name as the index

pokemon_df = pd.read_excel('data/pokemon.xlsx',
                           index_col=0, 
                           sheet_name="pokemon")

# Display the first 10 rows

pokemon_df.head(10)
