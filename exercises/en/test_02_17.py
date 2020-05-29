def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert fire_pokemon.shape == (52, 11), "Your dataframe imensions are incorrect. Are you selecting only the fire pokemons?"
    assert set(list(fire_pokemon.type)) == {'fire'} , "There are more than one pokemon types present. \n Are you selecting only fire pokemons?"
    __msg__.good("Nice work, well done!")