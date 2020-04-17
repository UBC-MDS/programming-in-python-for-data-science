import pandas as pd

# Read in the data from the csv file using the full pathway
# Save it as pokemon_sample   
# Only load in the first 100 rows and only load in columns  name, total_bs, type
# Display the dataframe

pokemon_sample = pd.read_csv('data/pokemon.csv',
                         nrows=100,
                         usecols=['name', 'total_bs', 'type'])

# Display the dataframe

pokemon_sample
