import numpy as np
import pandas as pd

candybar_df = pd.read_csv('data/candybars.csv', header=0, index_col=0)

print(candybar_df.head())

candybar_feats = list(candybar_df.columns)
print(candybar_feats)

candybar_names = list(candybar_df.index)
print(candybar_names)
print(len(candybar_names))

candybar_dim = candybar_df.shape
print(candybar_dim)