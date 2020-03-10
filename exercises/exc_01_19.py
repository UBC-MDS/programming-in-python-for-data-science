import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv', index_col = 0)

# Make an object named `position_column` that consists of just the `Position` column. 
# Note we will be using this for `value_counts` so we must do this with only using single `[]` brackets. 

____ = ____

# Find the frequencies of the position for the hockey team using `df.value_counts()` and save it as `position_freq`. Make sure you sort it too! 

# ____ = ____.____(____)

# Convert that to a dataframe. and save it as object `temp_df`
# ____ = ____.____(____)


# rename the column `Position` of `temp_df` to `freq` using `df.rename(columns = {})`. Save the object with the name `position_freq_df`. 
# ____ = ____.____(columns = ____)

# Display 
# ____