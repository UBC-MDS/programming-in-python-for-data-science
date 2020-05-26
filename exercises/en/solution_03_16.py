import pandas as pd

lego = pd.read_csv('data/lego-theme-hi.csv')
lego

# From the lego dataframe, make groups from the theme_name columns
# Find the max and min values for the num_parts column only using .agg()
# Stack the max and min values using .stack()
# Name the new dataframe stacked_lego

stacked_lego = (lego.groupby('theme_name')
                    .agg({'num_parts': ['max','min']})
                    .stack()
               )

# Display the dataframe

stacked_lego


