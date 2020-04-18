import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)

# Select the pokemon columns attack, defense, capture_rt, total_bs, and legendary 
# Save the new dataframe over object pokemon

____ = ____.____[____]
# ____

# Make a groupby object on the column legendary and name it pokemon_type

# ____ = ____.____(____)

# Make a new dataframe named legendary_stats using .agg() containing the max and min values of legendary groups

# ____ = ____.____(____) 
# ____

# Using .loc[] obtain from the legendary_stats dataframe, the following values:

# The capture rate (capture_rt) stats for non legendary (=0) pokemon and save them as object capture_0

# ____ = ____.____[____]
# ____

# The total base score (total_bs) stats for legendary (=1) pokemon and save them as object total_1

# ____ = ____.____[ ____]
# ____
