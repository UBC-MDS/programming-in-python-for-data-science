def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert  min(list(mighty_pokemon.defense)) == 101, "Are you selecting pokemons with attack and defense > 100?"
    assert mighty_pokemon.defense.sum() == 6693 , "Some values in the 'defense;'column is wrong. \n Are you selecting pokemons with defense > 100?"
    assert  max(list(mighty_pokemon.attack)) == 185, "Are you selecting pokemons with attack and defense > 100?"
    assert mighty_pokemon.attack.sum() == 6856 , "Some values in the 'attack' column is wrong. \n Are you selecting pokemons with attack > 100?"
    assert "&" in __solution__ , "Are you using the logic and operator '&'?"
    __msg__.good("Nice work, well done!")