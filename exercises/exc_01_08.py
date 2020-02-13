import numpy as np
import pandas as pd


candybar_df = pd.read_csv('data/candybars.csv', header=____, index_col=____)

print(candybar_df.head())

candybar_feats = ____(candybar_df.____)
print(candybar_feats)

candybar_names = ____(candybar_df.____)
print(candybar_names)
print(len(candybar_names))

candybar_dim = candybar_df.____
print(candybar_dim)