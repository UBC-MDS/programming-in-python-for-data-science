import pandas as pd

canucks = pd.read_csv('data/canucks.csv')

# Split up the column "Birth Date" into 3 separate columns named Birth_Day, Birth_Month and Birth_Year. 
# Name this new dataframe birthdate_df

birthdate_df = (canucks['Birth Date'].str.split('-', expand=True)
                                     .rename(columns={0:'Birth_Day',
                                                      1:'Birth_Month',
                                                    2: 'Birth_Year'})
             )
birthdate_df

# Save these as columns in the canucks dataframe as dtype int

canucks = canucks.assign(Birth_Day=birthdate_df['Birth_Day'].astype('int'),
                         Birth_Month=birthdate_df['Birth_Month'],
                         Birth_Year=birthdate_df['Birth_Year'].astype('int')
                        )




