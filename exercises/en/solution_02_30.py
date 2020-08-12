#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import altair as alt

pokemon = pd.read_csv('data/pokemon.csv')

pokemon_type = pd.DataFrame(pokemon.groupby('type').mean().loc[:, 'attack'
                         ].sort_values(ascending=False))

pokemon_type.reset_index(inplace=True)

attack_plot = alt.Chart(pokemon_type, width=500,
                        height=300).mark_bar().encode(x=alt.X('type:N',
        title='Pokemon type'), y=alt.Y('attack:Q',
        title='Mean attack score'
        )).properties(title='Mean attack value among Pokemon types')

attack_plot
			