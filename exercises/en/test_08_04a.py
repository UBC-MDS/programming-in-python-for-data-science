def test():
    import inspect
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "a_list" in __solution__, "Your object does not exist. Please make sure you are naming your object 'a_list'."
    assert "b_list" in __solution__, "Your object does not exist. Please make sure you are naming your object 'b_list'."
    assert len(a_list) == len(b_list), "Make sure both 'a_list' and 'b_list' are of the same length"
    __msg__.good("Nice work, well done!")