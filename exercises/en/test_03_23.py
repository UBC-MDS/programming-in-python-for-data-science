def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert lego_tower.shape[0] == 580255 and lego_tower.shape[1] == 10, "The lego_tower dataframe dimensions are incorrect. Are you merging properly?"
    assert "merge" in __solution__, "Make sure you are using the merge function."
    assert "color_id" in __solution__ and 'id' in __solution__, "Make sure you are merging on 'color_id' and 'id'."
    assert "outer" in __solution__, "Make sure you are doing an 'outer' join."
    assert "indicator=True" in __solution__, "Make sure to set the indicator variable to True."
    __msg__.good("Nice work, well done!")
