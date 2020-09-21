def test():
    import inspect
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "cleanup" in __solution__, "Your function does not exist. Please make sure you are naming your function 'cleanup'."
    str_fun = inspect.getsource(cleanup)
    assert 'data=data.loc[:, ~data.columns.duplicated()]' in str_fun, "Make sure you amending the 'cleanup' function to adhere to proper formatting."
    assert 'data = data[~data.duplicated(subset=columns, keep=False)]', "Make sure you amending the 'cleanup' function to adhere to proper formatting."
    __msg__.good("Nice work, well done!")