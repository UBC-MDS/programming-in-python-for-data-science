def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "family" in __solution__, "Make sure you are naming your object 'family'"
    assert "pd.DataFrame", "Make sure you are calling the 'pd.DataFrame()' in order to create the dataframe."
    assert family.shape[0] == 3 and family.shape[1] == 3, "The dimensions of your dataframe are incorrect. Are you specifying the correct data to the 'pd.DataFrame' function?"
    msg = "Your dataframe contains the incorrect columns. Are you specifying the correct column names? \
    \nExpected ['name', 'age', 'birth_month'], but got {0}".format(
        list(family.columns))
    assert sorted(list(family.columns)) == sorted(
        ['name', 'age', 'birth_month']), msg
    __msg__.good("Nice work, well done!")