def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "iloc" in __solution__ , "Are you using iloc to slice?"
    assert "11" in __solution__ , "You may be indexing the wrong position"
    assert "18" in __solution__ , "You may be indexing the wrong position"
    assert "0" in __solution__ , "You may be indexing the wrong position"
    assert "4" in __solution__ , "You may be indexing the wrong position"
    assert skilled_players.shape == (7, 4), "You may not have selected correctly "
    assert len(skilled_players) == 7, "You may not have selected correctly "
    assert list(skilled_players.columns) ==  ['Player', 'No.', 'Age', 'Height'], "Your columns do not seem to be correct"
    assert list(skilled_players.index) == [11, 12, 13, 14, 15, 16, 17], "Your rows do not seem to be correct"
    __msg__.good("Nice work, well done!")




