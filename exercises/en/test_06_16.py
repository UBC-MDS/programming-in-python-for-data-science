def test():
    import inspect
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "bmi_calculator" in __solution__, "Make sure you are naming your function 'bmi_calculator'"
    str_fun = inspect.getsource(bmi_calculator)
    assert str_fun.count('raise') == 2, "Make sure your are raising exceptions for all two conditions"
    assert 'TypeError' in str_fun, "Make sure you are raising a 'TypeError' for an incorrect data type"
    assert 'Exception' in str_fun, "Make sure you are raising a 'Exception' for an incorrect data value"
    __msg__.good("Nice work, well done!")