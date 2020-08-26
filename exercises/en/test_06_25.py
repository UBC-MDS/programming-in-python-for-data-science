def test():
    import inspect
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    str_fun = inspect.getsource(new_wage)
    assert not "for" in str_fun, "Make sure that you are not using any 'for' loops"
    assert round(person1_new_wage) == 94080, "Your function output is incorrect. Please revise and try again"
    assert new_wage(1000, 10.5) == 1105.0, "Your function output is incorrect. Please revise and try again"
    __msg__.good("Nice work, well done!")