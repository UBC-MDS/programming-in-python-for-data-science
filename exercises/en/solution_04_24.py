import pandas as pd

# Read in the data from the data folder named canucks.csv
# Name the dataframe canucks

canucks = pd.read_csv('data/canucks.csv')

# Find the mean height of the players
# Save it in an object named mean_height

mean_height = canucks['Height'].mean()

# What largest salary being paid to any of the players? 
# Save it in an object named max_salary

max_salary = canucks['Salary'].max()


