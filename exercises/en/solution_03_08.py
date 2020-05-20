import pandas as pd

lego = pd.read_csv('data/lego_untidy.csv', index_col=0)

# Convert the untidy data into tidy data using pivot_table 
# Make sure that you only assign set_num as your index
# Name the new dataframe tidied_lego
#

tidied_lego = (lego.reset_index()
                   .pivot_table(index=['set_num', 'name', 'year'],
                          columns='lego_info',
                          values='value')
                   .reset_index()
                   .set_index('set_num')
              )

# Display the first 5 rows

tidied_lego.head()


