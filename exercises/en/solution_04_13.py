import pandas as pd

ikea_items = {'item_name' : ['Bistro Set', 'Reclining Chair', 'Shelf Unit', 'Seat Pad', 'Shoe Rack'],
              'collection': ['APPLARO', 'APPLARO', 'HYLLIS', 'KUDDARNA', 'TJUSIG'],
              'price': [216.98, 80.00, 11.99, 29.99, 29.99]}

ikea_df = pd.DataFrame.from_dict(ikea_items)
ikea_df
