# Import pandas 
import pandas as pd

# Read in the dataset 
hockey_players = pd.read_csv('data/canucks.csv', index_col=0)


# Display the dataframe
hockey_players.head()