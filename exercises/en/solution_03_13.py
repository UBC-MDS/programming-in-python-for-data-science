import pandas as pd

lego = pd.read_csv('data/lego_untidy.csv')

# Convert the untidy data into tidy data using pivot_table 
# Assign set_num as your index and name the new dataframe tidied_lego

tidied_lego = (lego.pivot_table(index=['set_num', 'name', 'year'],
                                columns='lego_info',
                                values='value')
                   .reset_index()
              )

# Find the mean number of parts for each production year and save it in an object name year_parts_mean

year_parts_mean = tidied_lego.groupby('year').mean()[['num_parts']].round()

year_parts_mean
