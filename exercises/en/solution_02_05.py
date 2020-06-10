import pandas as pd

# Read in the data from the Excel file using the full pathway

pokemon_df = pd.read_excel('data/pokemon.xlsx', sheet_name="pokemon")

# Display the first 10 rows

pokemon_df.head(10)
