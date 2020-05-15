import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)
pokemon = pokemon.loc[ : , ['attack',  'defense', 'capture_rt', 'total_bs', 'legendary']]

# Make a groupby object on the column legendary 
# Find the maximum and minimum value of each column for each legendary groups using 
# .agg() and save the resulting dataframe as legendary_stats

legendary_stats = pokemon.groupby(by='legendary').agg(['max', 'min']) 

# Display it 

legendary_stats
