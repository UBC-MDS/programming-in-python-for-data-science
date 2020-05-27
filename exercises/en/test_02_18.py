def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "data/pokemon.csv" in __solution__ , "Are you specifying the correct data path?"
    assert "index_col=0" in __solution__ , "Are you making sure to add index_col=0 ?"
    assert  min(list(mighty_pokemon.defense)) == 101, "Are you selecting pokemons with defense > 100?"
    assert  min(list(mighty_pokemon.attack)) == 101, "Are you selecting pokemons with attack > 100?"
    assert "&" in __solution__ , "Are you using the logic and operator '&'?"
    __msg__.good("Nice work, well done!")