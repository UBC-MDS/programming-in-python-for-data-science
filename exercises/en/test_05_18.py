def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "count" in __solution__, "Make sure you are naming your object 'count'."
    assert "count = 0" in __solution__, "Make sure you are creating the 'count' variable and giving it a value of '0'"
    assert "for data in dataframes" in __solution__, "Make sure you are interating over 'dataframes'"
    assert ">" in __solution__, "Make sure you are checking if there are > 1000 rows"
    assert count == 1, "The value for 'count' is incorrect. Make sure you are incrementing 'count' if a dataframe has > 1000 rows"
    __msg__.good("Nice work, well done!")