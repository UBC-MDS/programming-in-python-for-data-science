def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "import pandas" in __solution__ , "Are you using the right commands to import pandas?"
    assert "read_csv" in __solution__ , "Are you reading in the data properly?"
    assert "index_col=0" in __solution__, "Are you making sure to add index_col=0 ?"
    assert hockey_players.shape == (22, 9), "You may not have the correct dataset"
    assert list(hockey_players.columns) ==  [ 'No.', 'Age', 'Height', 'Weight', 'Country', 'Position', 'Experience', 'Birth Date', 'Salary'], "Your column names do not seem correct"
    __msg__.good("Nice work, well done!")
