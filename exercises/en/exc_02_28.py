import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv')
pokemon = pokemon.loc[ : , ['attack',  'defense', 'capture_rt', 'total_bs', 'legendary']]

# Make a groupby object on the column legendary 
# Find the maximum and minimum value of each column for each legendary groups using 
# .agg() and save the resulting dataframe as legendary_stats

____ = ____.____[____].____(____) 

# Display it 

____


