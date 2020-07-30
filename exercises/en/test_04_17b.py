def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "Weight" in __solution__, "Make sure you are selecting only the 'Weight' column"
    assert "dtypes" in __solution__, "Make sure you are using the 'dtypes()` function to check the data type of the 'Weight' column."
    __msg__.good("Nice work, well done!")
