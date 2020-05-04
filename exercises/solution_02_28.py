import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv', index_col=0)

# Create a plot by chaining the following actions 
# Make a groupby object on the column type and name it pokemon_type
# Use .mean() on the new groupby object
# Use .loc[] to select the attack column
# Sort the pokemon mean attack values in descending order using .sort_values()
# Finally plot the graph and give it an appropriate title
# Name the object attack_plot 
# Name the y-axis "Attack scores"
 
attack_plot = (pokemon.groupby('type')
                      .mean()
                      .loc[:, 'attack']
                      .sort_values(ascending=False)
                      .plot.bar(title = 'Mean attack value among Pokemon types')
              )

attack_plot.set_ylabel('Attack score')