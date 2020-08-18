import pandas as pd
import altair as alt

pokemon = pd.read_csv('data/pokemon_sw.csv')

# Create an object using single brackets to obtain the column base_score and name it bs_column

bs_column = score_plot = pd.DataFrame(pokemon['base_score'])

# Plot the object bs_column using .mark_bar() and save this graph as score_plot

score_plot = alt.Chart(bs_column, width=500, height=300).mark_bar().encode(
    x='base_score',
    y='count()')

score_plot