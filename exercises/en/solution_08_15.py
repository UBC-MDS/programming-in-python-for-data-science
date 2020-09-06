import pandas as pd

canucks = pd.read_csv('data/canucks.csv')

# Identify any columns with null values with .info()
# Save this dataframe as canucks_info

canucks_info = canucks.info()
canucks_info

# Create a new column in the dataframe named Wealth
# where all the values equal "comfortable"
# Name the new dataframe canucks_comf

canucks_comf = canucks.assign(Wealth = "comfortable")
canucks_comf

# Do conditional replacement, where if the value in the salary column is null,
# we replace "comfortable" with "unknown" 

canucks_comf.loc[canucks_comf['Salary'].isnull(), "Wealth"] = "unknown"
canucks_comf