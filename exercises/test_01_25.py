def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert rich_players.shape == (22, 9), "Your dataframe is the wrong dimentions "
    assert 'sort_values' in __solution__ , "are you using sort_values?"
    assert 'ascending=False' in __solution__ , "are you sorting in descending order?"
    assert list(rich_players.columns) ==  ['No.', 'Age', 'Height', 'Weight', 'Country', 'Position',
 'Experience', 'Birth Date', 'Salary'], "Your columns do not seem to be correct for rich_players"
    assert list(rich_players.index) == ['Alexander Edler', 'Tyler Myers', 'J.T. Miller', 'Bo Horvat\xa0(C)',
       'Loui Eriksson', 'Brandon Sutter', 'Jacob Markstrom', 'Tanner Pearson', 'Antoine Roussel', 'Jay Beagle',
        'Jordie Benn', 'Troy Stecher', 'Tim Schaller', 'Jake Virtanen', 'Elias Pettersson', 'Zack MacEwen','Adam Gaudette',
         'Thatcher Demko', 'Guillaume Brisebois', 'Justin Bailey', 'Quinn Hughes', 'Christopher Tanev'], "Did you order in descending order?"
    __msg__.good("Nice work, well done!")
