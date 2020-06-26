def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "melt" in __solution__, "Make sure you are using the melt function."
    msg = "The tidied_lego dataframe contains the incorrect columns. Are you setting the correct id_vars? \
    \nExpected ['set_num', 'name', 'year', 'theme_id', 'num_parts', 'opacity', 'quantity'], but got {0}".format(
        list(tidied_lego.columns))
    assert sorted(list(tidied_lego.columns)) == sorted(['set_num', 'name', 'year', 'theme_id', 'num_parts', 'opacity', 'quantity']), msg
    assert set(tidied_lego.opacity) == {'matte', 'transparent'}, "Are you setting the value_vars to 'matte' and 'transparent'?"
    assert "quantity" in  __solution__, "Are you setting value_name to 'quantity?"
    __msg__.good("Nice work, well done!")
