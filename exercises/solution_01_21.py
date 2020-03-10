import pandas as pd

# Bring in previous frequency table we had saved as position_freq_df ignore this for now

position_freq_df = pd.read_csv('data/position_freq_df.csv', index_col=0)
position_freq_df

# Use `plot.bar()` with `position_freq`
# Assign a `color` as `Teal`, set opacity to 0.5 and don't forget to add a title as "Canuck Player Positions"  
position_bar = position_freq_df.plot.bar(color = "Teal", 
                                         alpha = .5, 
                                         title = "Canuck player positions")

position_bar
