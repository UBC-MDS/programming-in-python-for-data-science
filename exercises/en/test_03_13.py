def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "pivot_table" in __solution__, "Make sure you are using the pivot_table function."
    msg = "The tidied_lego dataframe contains the incorrect columns. Are you using the correct index column when pivoting? \
    \nExpected ['set_num', 'name', 'year', 'num_parts', 'theme_id'], but got {0}".format(
        list(tidied_lego.columns))
    assert sorted(list(tidied_lego.columns)) == sorted(['set_num', 'name', 'year', 'num_parts', 'theme_id']), msg
    assert "reset_index" in __solution__, "Are you resetting the index using .reset_index()?"
    assert "groupby" in __solution__, "Are you using the groupby function?"
    assert "year" in __solution__, "Are you grouping by year?"
    assert year_parts_mean.num_parts.sum() == 8093.0, "The mean values are incorrect. Are you taking the mean after grouping by year?"
    __msg__.good("Nice work, well done!")
