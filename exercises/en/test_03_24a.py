def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert lego_stock.shape[0] == 2846 and lego_stock.shape[1] == 7, "The lego_stock dataframe dimensions are incorrect. Are you merging properly?"
    assert "merge" in __solution__, "Make sure you are using the merge function."
    assert "set_num" in __solution__, "Make sure you are merging on 'set_num' from both tables."
    assert "inner" in __solution__, "Make sure you are doing an 'inner' join."
    assert "groupby" in __solution__, "Are you grouping by 'set_num'?"
    assert "ngroups" in __solution__, "Are you counting the number of groups using the 'ngroups' functon?"
    __msg__.good("Nice work, well done!")
