import pandas as pd

lego = pd.read_csv('data/lego-sets.csv')

# Convert the name column in the lego dataset to lowercase and save it in an object named lego 

lego = lego.assign(name = lego['name'].str.lower())


# Filter the dataset to find all the lego sets that contain "weetabix"
# Save this as a object named lego_weetabix

lego_weetabix = lego[lego['name'].str.contains('weetabix')]


# Replace the word "Weetabix" in the name column of the lego_wetabix dataframe
# with the string "cereal-brand"
# Save this in an object called lego_cereal

lego_cereal = lego_weetabix.assign(name = lego_weetabix['name'].str.replace('weetabix', 'cereal-brand'))


# If the row contains the word "promotional", change the entire value to "cereal-brand freebie"

lego_cereal.loc[lego_cereal['name'].str.contains('promotional'), 'name'] = 'cereal-brand freebie'


# Display lego_cereal

lego_cereal