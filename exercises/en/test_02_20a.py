def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "data/pokemon.csv" in __solution__ , "Are you specifying the correct data path?"
    assert "index_col=0" in __solution__ , "Are you making sure to add index_col=0 ?"
    assert "base_score" in list(pokemon.columns), "Are you creating a 'base_score' column?"
    assert  list(pokemon.base_score).count("strong") == 228, "Number of strong pokemon is incorrect. Are you selecting pokemons with total_bs >= 500?"
    assert  list(pokemon.base_score).count("weak") == 573, "Number of weak pokemon is incorrect. Are you selecting pokemons with total_bs < 500?"
    __msg__.good("Nice work, well done!")