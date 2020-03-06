def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert 'hockey_players[["Salary"]]' in __solution__ , "There seems to be a problem with getting all the rows from a single"
    assert '["Zack MacEwen", "Jake Virtanen", "Jordie Benn"]' in __solution__ , "It looks like there is a problem with the row labels you selected"
    assert '["Height", "Weight", "Salary", "Country"]' in __solution__ , "It looks like there is a problem with the columns labels you selected"
    assert (player_cost.sum() == 63325000.0).any, "Did you create player_cost properly?"
    assert penalty_players.shape == (3, 4), "You may not have selected correctly "
    assert len(penalty_players) == 3, "You may not have selected correctly "
    assert list(penalty_players.columns) ==  ['Height', 'Weight', 'Salary', 'Country'], "Your columns do not seem to be correct"
    assert list(penalty_players.index) == ['Zack MacEwen', 'Jake Virtanen', 'Jordie Benn'], "Your rows do not seem to be correct"
    __msg__.good("Nice work, well done!")
