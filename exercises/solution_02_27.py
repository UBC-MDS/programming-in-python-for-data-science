import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)
pokemon = pokemon.loc[ : , ['attack',  'defense', 'capture_rt', 'total_bs', 'legendary']]

# Make a groupby object on the column legendary and name it pokemon_legendary

pokemon_legendary = pokemon.groupby(by='legendary')

# Find the maximum and minimum value of each column for each legendary groups using 
# .agg() and save the resulting dataframe as legendary_stats.

legendary_stats = pokemon_legendary.agg(['max', 'min']) 
legendary_stats

# Obtain from the `legendary_stats` dataframe, the following values by using df.loc[]:

# The capture rate (capture_rt) stats for non legendary (=0) pokemon
# Save them as object capture_0

capture_0 = legendary_stats.loc[0, 'capture_rt']
capture_0

# The total base score (total_bs) stats for legendary (=1) pokemon
# Save them as object total_1

total_1 = legendary_stats.loc[ 1, 'total_bs']
total_1
