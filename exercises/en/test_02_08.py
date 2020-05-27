def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "data/pokemon.csv" in __solution__ , "Are you specifying the correct data path?"
    assert "nrows=100" , "Are you using nrows=100 to select the first 100 rows?"
    assert sorted(list(pokemon_sample.columns)) == ['name', 'total_bs', 'type'], "Are you setting use_cols = ['name', 'total_bs', 'type'] ?"
    __msg__.good("Nice work, well done!")

