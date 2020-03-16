def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "bar" in __solution__ , "You don't seem to be plotting a bar chart "
    assert 'alpha = 0.5' in __solution__ , "Your alpha value is not correct"
    assert 'color = "Teal"' in __solution__ , "Your colour assignment is not correct"
    assert 'title = "Canuck player positions"' in __solution__ , "Your title  is not correct"
    __msg__.good("Nice work, well done!")