def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert benched_players.shape == (7, 9), "You may not have sliced correctly "
    assert len(benched_players) == 7, "You may not have sliced correctly "
    assert list(benched_players.columns) ==  ['No.', 'Age', 'Height', 'Weight', 'Country', 'Position', 'Experience', 'Birth Date', 'Salary'], "Your columns do not seem to be correct"
    assert list(benched_players.index) == ['Guillaume Brisebois','Thatcher Demko','Alexander Edler', 'Loui Eriksson','Adam Gaudette', 'Bo Horvat\xa0(C)', 'Quinn Hughes'], "Your rows do not seem to be correct"
    __msg__.good("Nice work, well done!")
    
