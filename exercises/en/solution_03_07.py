import pandas as pd

lego = pd.read_csv('data/lego_untidy.csv', index_col=0)
lego

lego.reset_index().pivot(index='set_num', columns='lego_info', values='value')


