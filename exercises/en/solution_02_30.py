import pandas as pd

pokemon = pd.read_csv('data/pokemon.csv')

# Create a plot by chaining the following actions 
# Make a groupby object on the column type and name it pokemon_type
# Use .mean() on the new groupby object
# Use .loc[] to select the attack column
# Sort the pokemon mean attack values in descending order using .sort_values()
# Finally plot the graph and give it an appropriate title
# Name the y-axis "Mean attack scores"
# Name the object attack_plot 
 
attack_plot = (pokemon.groupby('type')
                      .mean()
                      .loc[:, 'attack']
                      .sort_values(ascending=False)
                      .plot.bar(title = 'Mean attack value among Pokemon types')
                      .set_ylabel('Mean attack score')
              )
