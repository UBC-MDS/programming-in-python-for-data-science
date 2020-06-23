import pandas as pd

pokemon = pd.read_csv('data/pokemon_sw.csv')

# Create an object using single brackets to obtain the column base_score and name it bs_column

bs_column = pokemon['base_score']

# Find the frequency of each using .value_counts() and save this as object score_freq

score_freq = bs_column.value_counts()

# Plot the object score_freq using .plot.bar() and save this graph as score_plot

score_plot = score_freq.plot.bar()