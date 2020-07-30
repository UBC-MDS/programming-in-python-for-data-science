def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "birthdate_df" in __solution__, "Make sure you are naming your result 'birthdate_df'."
    assert "str.split" in __solution__, "Make sure you are using the 'str.split' function to split the 'Birth Date' column."
    assert "canucks.assign" in __solution__, "Make sure to use the '.assign' function to reassign the data types of the required columns."
    assert str(canucks['Birth_Day'].dtype) == "int64", "Make sure you are reassigning the 'Birth_day' column to type 'int'."
    assert str(canucks['Birth_Month'].dtype) == "int64", "Make sure you are reassigning the 'Birth_Month' column to type 'int'."
    assert str(canucks['Birth_Year'].dtype) == "int64", "Make sure you are reassigning the 'Birth_Year' column to type 'int'."
    __msg__.good("Nice work, well done!")
