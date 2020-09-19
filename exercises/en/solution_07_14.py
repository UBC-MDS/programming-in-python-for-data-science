import pandas as pd
def cleanup(data, columns):
    """
    This removed any duplicate column names or any duplicate
    rows in the dataframe. Duplicate rows are decided based on the columns
    argument

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
    """

    # Drop duplicate columns
    data=data.loc[:, ~data.columns.duplicated()]  
    
    # Drop duplicate rows
    data = data[~data.duplicated(subset=columns, keep=False)]



    return data

