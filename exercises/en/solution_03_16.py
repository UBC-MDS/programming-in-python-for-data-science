import pandas as pd

lego = pd.read_csv('data/lego_untidy2.csv')

# Melt the dataframe and name the values column quantity  
# Name your dataframe tidied_lego

tidied_lego = (lego.melt(id_vars=['set_num', 'name', 'year', 'theme_id', 'num_parts'],
                         value_vars=['matte', 'transparent'],
                         var_name='opacity',
                         value_name= 'quantity')
              )

# Display the dataframe

tidied_lego
