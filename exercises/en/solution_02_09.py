import pandas as pd

# Read in the data from the csv file using the full pathway
# Save it as pokemon_df2
# Use the pokemon name as the index          
# Change the values in column legendary from yes to True the values no, to False     
# Only load in the columns named attack, defense, speed, type and legendary    

pokemon_df2 = pd.read_csv('data/pokemon2.csv',
                          index_col=0,
                          header=4,
                          usecols=['attack', 'defense', 'speed', 'type', 'legendary'], 
                          true_values= ['yes'],
                          false_values= ['no'] )

# Display the dataframe

pokemon_df2
