import pandas as pd

DAYS_PER_YEAR = 365.25

# Read in the canucks.csv file from the data folder and parse the "Birth Date" column
# Save this as an object named canucks

canucks = pd.read_csv('data/canucks.csv', parse_dates = ['Birth Date'])

# Find the oldest player's date of birth 
# Save the Timstamp as oldest

oldest = canucks['Birth Date'].min()

# Find the youngest player's date of birth 
# Save the Timstamp as yongest

youngest = canucks['Birth Date'].max()

# Find the age difference between the two players in number of years to 2 decimal places
# Save this an an object name age_range

age_range = round((youngest - oldest).days/DAYS_PER_YEAR, 2)

# Display age_range

age_range
