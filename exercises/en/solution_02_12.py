import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)

# Drop the columns deck_no, capture_rt, and legendary
# Make sure to overwrite the new dataframe to object pokemon

pokemon = pokemon.drop(columns=['deck_no', 'capture_rt', 'legendary'])

# Display the first 5 rows of the dataframe

pokemon.head()
