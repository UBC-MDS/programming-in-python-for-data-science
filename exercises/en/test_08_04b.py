def test():
    import inspect
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "a_array" in __solution__, "Your object does not exist. Please make sure you are naming your object 'a_array'."
    assert "a_array" in __solution__, "Your object does not exist. Please make sure you are naming your object 'b_array'."
    assert "==" in __solution__, "Make sure you are checking equality using the '==' operator"
    assert len(a_array) == len(b_array), "Make sure both 'a_array' and 'b_array' are of the same length"
    __msg__.good("Nice work, well done!")