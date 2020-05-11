import pandas as pd

# Load in the csv named "position_frequencies.csv" you made in exercise 24 and save it as `position_freq`. 

position_freq = pd.read_csv('data/position_freq_df.csv', index_col=0)

position_freq

# Use `plot.bar()` with `position_freq`.
# Assign a `color` as `Teal`and set opacity to 0.5.      
# Don't forget to add a title as "Canuck Player Positions". 

position_bar = position_freq.plot.bar(color='Teal', 
                                         alpha=0.5, 
                                         title='Canuck player positions')
