def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "concat" in __solution__, "Make sure you are using the concat function."
    assert "axis=1" in __solution__, "Make sure you are concatenating horizontally using 'axis=1'."
    msg = "The lego_full dataframe contains the incorrect columns. Are you setting the correct id_vars? \
    \nExpected ['set_num', 'name', 'year', 'theme_id', 'matte', 'transparent', 'total_pieces'], but got {0}".format(
        list(lego_full.columns))
    assert sorted(list(lego_full.columns)) == sorted(['set_num', 'name', 'year', 'theme_id', 'set_num', 'matte', 'transparent']), msg
    assert lego_full.shape[0] == 11673 and lego_full.shape[1] == 7, "The lego_full dataframe dimensions are incorrect. Are you concatenating horizontally?"
    assert "duplicated" in __solution__, "Are you removing duplicates using the .duplicates() function?"
    assert sorted(list(washed_lego.columns)) == sorted(['set_num', 'name', 'year', 'theme_id', 'matte', 'transparent']), msg
    assert 'total_pieces' in list(lego_details.columns), "Have you added the total_pieces column?"
    assert list(lego_details.total_pieces)[1:5] == [5462.0, 5217.0, 5200.0, 4788.0], "Are you sorting the total_pieces column in descending order?"
    __msg__.good("Nice work, well done!")
