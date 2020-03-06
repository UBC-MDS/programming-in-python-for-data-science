def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "iloc" in __solution__ , "Are you using iloc to slice?"
    assert "[16, 4, 21, 1]" in __solution__ , "You may be indexing the wrong position"
    assert "[0, 8, 7, 9]" in __solution__ , "You may be indexing the wrong position"
    assert injured_players.shape == (4, 4), "You may not have selected correctly "
    assert len(injured_players) == 4, "You may not have selected correctly "
    assert list(injured_players.columns) ==  ['Player', 'Birth Date', 'Experience', 'Salary'], "Your columns do not seem to be correct"
    assert list(injured_players.index) == [16, 4, 21, 1], "Your rows do not seem to be correct"
    __msg__.good("Nice work, well done!")