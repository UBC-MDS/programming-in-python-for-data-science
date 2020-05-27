def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "data/pokemon.csv" in __solution__ , "Are you specifying the correct data path?"
    assert "index_col=0" in __solution__ , "Are you making sure to add index_col=0 ?"
    assert fire_pokemon.shape == (52, 11), "Dimensions are incorrect. Are you selecting only the fire pokemons?"
    assert set(list(fire_pokemon.type)) == {'fire'}
    __msg__.good("Nice work, well done!")