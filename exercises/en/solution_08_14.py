import pandas as pd

canucks = pd.read_csv('data/canucks.csv')

# Replace the null values in the dataframe with the mean salary value
# Save this as a new dataframe named canucks_altered

canucks_altered = canucks.fillna(value=canucks['Salary'].mean())

# Display the canucks_altered dataframe

canucks_altered