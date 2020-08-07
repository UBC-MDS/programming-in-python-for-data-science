def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "integer_list" in __solution__, "Make sure you are naming your object 'integer_list'."
    assert "integer_list = list()", "Make sure you are creating a new list with the 'list()' function"
    assert "for i in float_list", "Make sure you are iterating over the contents of 'float_list'"
    assert "integer_list.append", "Make sure you are appending to 'integer_list' using the 'append()' function"
    assert sum(integer_list) == 160, "The values in 'integer_list' are incorrect. Are you converting to 'int' and appending after?"
    __msg__.good("Nice work, well done!")