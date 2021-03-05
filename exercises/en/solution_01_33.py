import pandas as pd
import altair as alt

# The data

hockey_players = pd.read_csv('data/canucks.csv', index_col=0)

# Plots x as Age and y as Salary using a scatterplot
# Set color to Darkblue and opacity to 0.4
# Don't forget to assign a title as "Canuck players Age vs. Salary"

age_salary_scatter = alt.Chart(
    hockey_players, width=500, height=300).mark_circle(
        color='Darkblue', opacity=0.4).encode(
            x='Age',
            y='Salary').properties(title='Canuck players Age vs. Salary')

age_salary_scatter