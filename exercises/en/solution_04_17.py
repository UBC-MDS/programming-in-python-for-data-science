import pandas as pd

# Read in the data from the data folder named `canucks.csv` 
# Name the dataframe `canucks`

canucks = pd.read_csv('data/canucks.csv')

canucks.dtypes

# type(canucks)
# type(canucks['Country'])
# type(canucks[['Country']])