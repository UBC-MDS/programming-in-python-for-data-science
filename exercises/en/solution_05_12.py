# Load in the packages

import pandas as pd

# Starting with an empty dataframe

full_dataframe = None

# This code creates loop that reads in each dataframe and concatenates them together

for number in range(1,5):
    string = 'data/pkm' + str(number) + '.csv'
    data = pd.read_csv(string)
    full_dataframe = pd.concat([full_dataframe,data])

# Display the final dataframe

full_dataframe