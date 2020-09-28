import pandas as pd

lego = pd.read_csv('data/lego_untidy.csv')

# Convert the untidy data into tidy data using pivot 
# Name the new dataframe tidied_lego

tidied_lego = pd.DataFrame(lego.pivot(index='set_num',
                          columns='lego_info',
                          values='value')
                   .reset_index()
              )

# Save the mean number of parts (num_parts) of the Lego sets in an object named set_parts_mean

set_parts_mean = tidied_lego[['num_parts']].mean().round()

set_parts_mean


