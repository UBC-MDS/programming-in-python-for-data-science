def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "ikea_items" in __solution__, "Make sure you are naming your object 'ikea_items'."
    assert "ikea_df" in __solution__, "Make sure you are naming your object 'ikea_df'."
    msg = "Your ikea_items dictionary contains the incorrect keys. Are you adding all the items? \
    \nExpected ['item_name', 'collection', 'price'], but got {0}".format(
        list(ikea_items.keys()))
    assert sorted(list(ikea_items.keys())) == sorted(
        ['item_name', 'collection', 'price']), msg
    assert sorted(ikea_items['item_name']) == [
        'Bistro Set', 'Shelf Unit', 'Shoe Rack'
    ], "The 'item_name' key contains the wrong values. Make sure you are reading the table correctly"
    assert sorted(ikea_items['collection']) == [
        'APPLARO', 'HYLLIS', 'TJUSIG'
    ], "The 'collection' key contains the wrong values. Make sure you are reading the table correctly"
    assert sorted(ikea_items['price']) == [
        11.99, 29.99, 216.98
    ], "The 'price' key contains the wrong values. Make sure you are reading the table correctly"
    assert "pd.DataFrame.from_dict" in __solution__, "Make sure you are converting the dictionary to a dataframe using the 'pd.DataFrame.from_dict()' function."
    __msg__.good("Nice work, well done!")
