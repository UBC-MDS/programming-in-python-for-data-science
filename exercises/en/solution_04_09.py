import pandas as pd

# Use the lists below to make a dataframe named family

mom = ['Teresa', 57, "August"]
dad = ['John', 61, "February"]
brother = ['Desmond', 5, "July" ]

c_names = ['name', 'age', 'birth_month']

family = pd.DataFrame(data=[mom, dad, brother], 
                       columns=c_names)

family
