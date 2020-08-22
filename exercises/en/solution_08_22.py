import pandas as pd

canucks = pd.read_csv('data/canucks.csv', parse_dates = ['Birth Date'])

# Convert the Position and Country columns into uppercase 
# Save this in a dataframe named canucks_upper

canucks_upper = canucks.assign(Position = canucks['Position'].str.upper(),
                               Country = canucks['Country'].str.upper())

# Create a new column in the canucks_upper dataframe named number_ts
# where you count the total number of times the letter T (lowercase or uppercase) appears in their name
# Save this  dataframe named as canucks_upper_ts

canucks_upper_ts = canucks_upper.assign(number_ts = canucks_upper['Player'].str.lower().str.count('t'))

# How many players have more than 1 letter T in their name? 

canucks_upper_ts[canucks_upper_ts['number_ts'] > 1].shape[0]
