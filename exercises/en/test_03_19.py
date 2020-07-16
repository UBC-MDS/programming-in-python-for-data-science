def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "concat" in __solution__, "Make sure you are using the concat function."
    assert "axis=0" in __solution__, "Make sure you are concatenating vertically using 'axis=0'."
    msg = "The full_set dataframe contains the incorrect columns. Are you setting the correct id_vars? \
    \nExpected ['set_num', 'name', 'year', 'theme_id', 'num_parts'], but got {0}".format(
        list(full_set.columns))
    assert sorted(list(full_set.columns)) == sorted(['set_num', 'name', 'year', 'theme_id', 'num_parts']), msg
    assert full_set_shape[0] == 11673 and full_set_shape[1] == 5, "The full_set dataframe dimensions are incorrect. Are you concatenating vertically?"
    __msg__.good("Nice work, well done!")
