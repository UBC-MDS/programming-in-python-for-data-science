def test():
    import inspect
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "bmi_calculator" in __solution__, "Make sure you are naming your function 'bmi_calculator'"
    str_fun = inspect.getsource(bmi_calculator)
    assert "Parameters" in str_fun, "Make sure your docstring includes a 'Parameter' section"
    assert "height" in str_fun.lower(), "Make sure you are describing the 'height' argument in the docstring"
    assert "weight" in str_fun.lower(), "Make sure you are describing the 'weight' argument in the docstring"
    assert "Returns" in str_fun, "Make sure your docstring includes a 'Returns' section"
    assert "Examples" in str_fun, "Make sure your docstring includes an 'Examples' section"
    __msg__.good("Nice work, well done!")