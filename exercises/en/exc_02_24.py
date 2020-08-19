import pandas as pd
import altair as alt

pokemon = pd.read_csv('data/pokemon.csv')

# First, rename the column `capture_rt` to `capture_rate`.
# Then, create a new column named `AD_total` by adding the `attack` and `defense` columns from the pokemon dataset.
# Save this in a dataframe object called `plot_df`.
# ____ = pd.DataFrame(____.____(columns={'____': '____'})
#                       .____(____=pokemon['____'] + pokemon['____'])
#                )

# Use .mark_circle() to plot AD_total on the x-axis  and capture_rt on the y-axis
# Name the plot pokemon_plot
# pokemon_plot = alt.Chart(____, width=500, height=300).____().____(
#    x='____',
#    y='____')

#pokemon_plot