import pandas as pd

# Read in the data from the data folder named `canucks.csv` 
# Name the dataframe `canucks`

canucks = pd.read_csv('data/canucks.csv')

# Use the dtypes attribute on the whole dataframe 
# Save the output as canuck_types 

canuck_types = canucks.dtypes

canuck_types