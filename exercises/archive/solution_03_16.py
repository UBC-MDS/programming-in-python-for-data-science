import pandas as pd

lego = pd.read_csv('data/lego-theme-hi.csv')
lego

# Follow the tasks above and name the new dataframe stacked_lego

stacked_lego = (lego.groupby('theme_name')
                    .agg({'num_parts': ['max','min']})
                    .stack()
               )

# Display the dataframe

stacked_lego


