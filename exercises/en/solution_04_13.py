import pandas as pd

ikea_items = {'item_name' : ['Bistro Set', 'Shelf Unit', 'Shoe Rack'],
              'collection': ['APPLARO', 'HYLLIS', 'TJUSIG'],
              'price': [216.98, 11.99, 29.99]}

ikea_df = pd.DataFrame.from_dict(ikea_items)
ikea_df
