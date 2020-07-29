def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "together" in __solution__, "Make sure you are naming your result 'together'."
    assert "str" in __solution__, "Make sure you are converting 'numerical1' to type string using the 'str' function."
    assert "+" in __solution__, "Make sure you are using the '+ operator to combine 'string1' and 'numerical1'."
    assert type(
        together
    ) is str, "Make sure you are concatenating 'string1' and 'numerical1' as strings."
    __msg__.good("Nice work, well done!")