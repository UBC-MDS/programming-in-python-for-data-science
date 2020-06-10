def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "[10, 21, 2]" in __solution__ , "It looks like there is a problem with the row labels you selected"
    assert penalty_players.shape == (3, 4), "You may not have selected correctly "
    assert len(penalty_players) == 3, "You may not have selected correctly "
    assert list(penalty_players.columns) ==  ['Height', 'Weight', 'Salary', 'Country'], "Your columns do not seem to be correct"
    assert list(penalty_players.index) == [10, 21, 2], "Your rows do not seem to be correct"
    __msg__.good("Nice work, well done!")
