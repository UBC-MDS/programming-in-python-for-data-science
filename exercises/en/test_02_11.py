def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "rename" in __solution__ , "Are you using the 'rename' function?"
    assert not {"sp_attack"}.issubset(set(pokemon_special.columns)), "Are you changing 'sp_attack' to 'special_a' using ':'?"
    assert not {"sp_defense"}.issubset(set(pokemon_special.columns)), "Are you changing 'sp_defense' to 'special_d' using ':'?"
    __msg__.good("Nice work, well done!")

