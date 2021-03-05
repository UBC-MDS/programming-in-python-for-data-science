import pandas as pd
import altair as alt

# Load in the csv named "canucks.csv" the same way you did earlier
# Save it as hockey_players

hockey_players = pd.read_csv('data/canucks.csv', index_col=0)

hockey_players

# Use alt.Chart() to create a chart object
# Use the .mark_bar() to create a bar plot
# Use the .encode() to specify the column to plot
# Assign a color as Teal and set opacity to 0.5
# Don't forget to add a title as "Canuck Player Positions"

position_bar = alt.Chart(
    hockey_players, width=500, height=300).mark_bar(
        color='Teal', opacity=0.5).encode(
            x='Position',
            y='count()').properties(title='Canuck player positions')

position_bar
