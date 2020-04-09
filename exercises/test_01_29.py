def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert 'bar' in __solution__ , "You don't seem to be plotting a bar chart "
    assert position_freq.shape == (3, 1), "Did you load in position_freq correctly?"
    assert 'alpha' in __solution__ , "You have not specified an alpha parameter"
    assert '0.5' in __solution__ , "Your alpha value is not correct"
    assert 'color' in __solution__ , "Your have not specified a color parameter"
    assert '"Teal"' in __solution__ , "Your colour parameter is not correct"
    assert 'title' in __solution__ , "You have not specified a title"
    assert '"Canuck player positions"' in __solution__ , "Your title is not correct"
    assert "position_freq"in __solution__ , "the dataframe you are calling is not correct"
    __msg__.good("Nice work, well done!")
