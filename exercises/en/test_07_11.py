def test():
    import inspect
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert 'test_find_force' in __solution__, 'Your function does not exist. Please make sure you are naming your function test_find_force.'
    str_fun = inspect.getsource(test_find_force)
    assert str_fun.count('assert') == 3, 'Make sure you are including all the assert statements.'
    assert str_fun.count('find_force(50, 3)') == 1, 'Make sure you are including all the assert statements.'
    assert str_fun.count('find_force(100, -2)') == 1, 'Make sure you are including all the assert statements.'
    assert str_fun.count('find_force(5, 20)') == 1, 'Make sure you are including all the assert statements.'
    __msg__.good("Nice work, well done!")