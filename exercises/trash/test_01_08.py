def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert benched_players.shape == (13, 6), "You may not have sliced correctly "
    assert len(benched_players) == 13, "You may not have sliced correctly "
    assert list(benched_players.columns) ==  ['Player', 'No.', 'Age', 'Height', 'Weight', 'Country'], "Your columns do not seem to be correct"
    assert list(benched_players.index) == [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], "Your rows do not seem to be correct"
    __msg__.good("Nice work, well done!")
