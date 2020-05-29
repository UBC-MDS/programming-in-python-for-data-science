def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "drop" in __solution__ , "Are you using the 'drop' function on the dataframe?"
    assert not {'deck_no'}.issubset(set(pokemon.columns)) , "Have you dropped the 'deck_no' column?"
    assert not {"capture_rt"}.issubset(set(pokemon.columns)) , "Have you dropped the 'capture_rt' column?"
    assert not {"legendary"}.issubset(set(pokemon.columns)) , "Have you dropped the 'legendary' column?"
    __msg__.good("Nice work, well done!")
