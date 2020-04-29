import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)
pokemon = pokemon.loc[ : , ['attack',  'defense', 'capture_rt', 'total_bs', 'legendary']]

# Make a groupby object on the column legendary and name it pokemon_legendary

____ = ____.____[____]

# Find the maximum and minimum value of each column for each legendary groups using 
# .agg() and save the resulting dataframe as legendary_stats.

# ____ = ____.____(____) 
# ____

# Obtain from the `legendary_stats` dataframe, the following values by using df.loc[]:

# The capture rate (capture_rt) stats for non legendary (=0) pokemon
# Save them as object capture_0

# ____ = ____.____[____]
# ____

# The total base score (total_bs) stats for legendary (=1) pokemon
# Save them as object total_1

# ____ = ____.____[ ____]
# ____
