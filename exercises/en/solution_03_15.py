import pandas as pd

lego = pd.read_csv('data/lego-sets.csv', index_col=0)
lego

# melt the dataframe columns matte and transparent into a single column named opacity and name the values column quantity  
# Name the new dataframe tidied_lego 
# Assign set_num ad the index in your new dataframe  

tidied_lego = (lego.reset_index()
                   .melt(id_vars=['set_num', 'name', 'year', 'theme_id', 'num_parts'],
                         value_vars=['matte', 'transparent'],
                         var_name='opacity',
                         value_name='quantity')
                   .set_index('set_num')
              )

# Display the dataframe

tidied_lego
