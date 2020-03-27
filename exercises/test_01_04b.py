def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "hockey_shape = hockey_players.shape" in __solution__ , "There seems to be a problem with the dimension of the datset"
    assert hockey_shape == (22, 9), "You may not have the correct dataset"
    __msg__.good("Nice work, well done!")
