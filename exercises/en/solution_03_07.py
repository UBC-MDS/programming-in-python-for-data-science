import pandas as pd

lego = pd.read_csv('data/lego_untidy.csv', index_col=0)

# Convert the untidy data into tidy data using pivot 
# Name the new dataframe tidied_lego

tidied_lego = (lego.reset_index()
                   .pivot(index='set_num',
                          columns='lego_info',
                          values='value')
              )

# Display the first 5 rows

tidied_lego.head()


