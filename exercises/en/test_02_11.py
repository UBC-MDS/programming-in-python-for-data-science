def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "data/pokemon.csv" in __solution__ , "Are you specifying the correct data path?"
    assert "index_col=0" in __solution__ , "Are you making sure to add index_col=0 ?"
    assert "sp_attack':'special_a" , "are you changing 'sp_attack' to 'special_a' using ':' "
    assert "sp_defense':'special_a" , "are you changing 'sp_defense' to 'special_d' using ':' "
    __msg__.good("Nice work, well done!")

