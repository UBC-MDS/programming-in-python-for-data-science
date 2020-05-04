import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)
pokemon = pokemon.loc[ : , ['attack',  'defense', 'capture_rt', 'total_bs', 'legendary']]

# Make a groupby object on the column legendary 
# Find the maximum and minimum value of each column for each legendary groups using 
# .agg() and save the resulting dataframe as legendary_stats

legendary_stats = pokemon.groupby(by='legendary').agg(['max', 'min']) 
legendary_stats

# Obtain from the legendary_stats dataframe the capture rate (capture_rt)
# for non legendary (=0) pokemon using df.loc[]
# Save this as object nonlegend_cap_rate

nonlegend_cap_rate = legendary_stats.loc[0, 'capture_rt']

# Display it 

nonlegend_cap_rate
