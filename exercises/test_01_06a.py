def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "columns_hockey = hockey_players.columns" in __solution__ , "There seems to be a problem with finding the column names of the dataset"
    assert list(columns_hockey) ==  ['No.', 'Age', 'Height', 'Weight', 'Country', 'Position', 'Experience', 'Birth Date', 'Salary'], "Your column names do not seem correct"
    __msg__.good("Nice work, well done!")
