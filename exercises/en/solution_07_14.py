import pandas as pd

def cleanup(data, columns):
    '''
    This removes any duplicate column names or any duplicate
    rows in the dataframe.

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        The dataframe to clean
    param2 : list
        A list of columns to determine which are duplicated rows

    Returns
    -------
    pandas.core.frame.DataFrame
        A dataframe with unique columns and rows

    Examples
    --------
    >>> cleanup(bakery,['bread'])
    bread	    quantity
	white	       4
    rye	           6
    wholegrain     2
    '''

    # Drops duplicate columns
    data = data.loc[:, ~data.columns.duplicated()]  
    
    # Drops duplicate rows
    data = data[~data.duplicated(subset=columns, keep=False)]

    return data

