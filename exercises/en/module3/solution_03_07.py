import pandas as pd

lego = pd.read_csv('data/lego-sets.csv', index_col=0)
lego

# +
new = (lego.reset_index()
     .melt(id_vars=['set_num'], 
           value_vars=['theme_id', 'num_parts'],
           var_name="lego_info",
           value_name="value")
     .sort_values('set_num').set_index('set_num')
     
)
new.to_csv('lego_untidy.csv')
# -

lego = pd.read_csv('data/lego-themes.csv', index_col=0)
lego

# +
new = (lego.reset_index()
           .pivot(index=['set_num'], 
                 columns=['theme_id', 'num_parts'],
                 var_name="lego_info",
                 value_name="value")
           .sort_values('set_num').set_index('set_num')
         
)
new.to_csv('lego_untidy.csv')
# -

df.pivot(index=['index label'], columns='column_name', values='new_colum_name')
df to e
