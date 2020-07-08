def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert lego_stock.shape[0] == 2846 and lego_stock.shape[1] == 8, "The lego_stock dataframe dimensions are incorrect. Are you merging properly?"
    assert store_inventory.quantity.sum() == 3916, "The sum of the values in the quantity column is incorrect. Are you grouping by set_num and taking the sum?"
    assert "set_num" in __solution__, "Are you using 'set_num' to group and merge?"
    assert "merge" in __solution__, "Make sure you are using the merge function."
    assert "inner" in __solution__, "Make sure you are doing an 'inner' join."
    assert "groupby" in __solution__, "Are you grouping by 'set_num'?"
    assert ".agg" in __solution__, "Are you using the aggregate function 'agg' to sum up the 'quantity' column?"
    assert "sort_values" in __solution__, "Are you sorting the 'quantity' column?"
    assert round(store_inventory_details.num_parts.mean()) == 80.0, "The average of the num_parts column for the store_inventory_details dataframe is incorrect. Are you doing an inner merge on set_num?"
    assert list(store_inventory_details.quantity)[1:5] == [60, 60, 60, 60], "Are you sorting the quantity column in descending order?"
    __msg__.good("Nice work, well done!")
