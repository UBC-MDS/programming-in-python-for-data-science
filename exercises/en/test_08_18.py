def test():
    import inspect
    import numpy as np
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "canucks" in __solution__, "Your object does not exist. Please make sure you are naming your object 'canucks'."
    assert "parse_dates" in __solution__, "Make sure you are using the 'parse_dates' argument when reading in the data."
    assert str(canucks['Birth Date'].dtypes) == 'datetime64[ns]', "The 'Birth Date' column is of the incorrect data type. Are you parsing it as datetime?"
    assert str(youngest) == "1999-10-14 00:00:00", "The value for 'youngest' is incorrect. Are you using the '.min()' function?"
    assert str(oldest) == "1985-07-17 00:00:00", "The value for 'oldest' is incorrect. Are you using the '.max()' function?"
    assert age_range == 14.24, "The value for 'age_range' is incorrect. Are you computing the 'oldest' and 'youngest' correctly?"
    __msg__.good("Nice work, well done!")