import pandas as pd

lego = pd.read_csv('data/lego_untidy.csv', index_col=0)
lego

lego.pivot(index=['index label'], columns='column_name', values='new_colum_name')


