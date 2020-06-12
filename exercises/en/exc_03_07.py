import pandas as pd

lego = pd.read_csv('data/lego_untidy.csv')

# Convert the untidy data into tidy data using pivot 
# Name the new dataframe tidied_lego

____ = (____.pivot(index=____,
                   columns=____,
                   values=____)
            .____()
       )

# Save the mean number of parts (num_parts) of the Lego sets in an object named set_parts_mean

____ = ____[[____]].____().round()

____

# ____
