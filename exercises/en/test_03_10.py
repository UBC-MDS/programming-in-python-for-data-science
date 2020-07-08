def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert ".pivot" in __solution__, "Make sure you are using the pivot function."
    assert "reset_index" in __solution__, "Are you resetting the index using .reset_index()?"
    assert "set_num" in __solution__, "Are you setting the index to 'set_num'?"
    assert set_parts_mean[0] == 162.0, "The mean value is incorrect. Are you using the .mean() function?"
    __msg__.good("Nice work, well done!")
