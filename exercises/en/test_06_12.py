def test():
    import inspect
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "bmi_calculator" in __solution__, "Make sure you are naming your function 'bmi_calculator'"
    str_fun = inspect.getsource(bmi_calculator)
    assert "parameters" in str_fun.lower(), "Make sure your docstring includes a 'Parameter' section"
    assert "height" in str_fun.lower(), "Make sure you are describing the 'data' paratemter in the docstring"
    assert "weight" in str_fun.lower(), "Make sure you are describing the 'grouping_col' paratemter in the docstring"
    assert "returns" in str_fun.lower(), "Make sure your docstring includes a 'Returns' section"
    assert "examples" in str_fun.lower(), "Make sure your docstring includes an 'Examples' section"
    __msg__.good("Nice work, well done!")