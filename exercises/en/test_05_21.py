def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "def" in __solution__, "Make sure you are defining a function"
    assert "uppercase_count" in __solution__, "Make sure you are naming your function 'uppercase_count'"
    assert string2 == 7, "Your function output is incorrect. Are you converting properly?"
    __msg__.good("Nice work, well done!")