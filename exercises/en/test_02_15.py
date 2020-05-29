def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "assign" in __solution__ , "Are you using the 'assign' function to create the new column?"
    assert "total_special" in __solution__ , "Are you naming the new column 'total_special'?"
    assert sum(pokemon.total_special) == 113906, "Values in the column 'total_special' is wrong. Are you adding 'sp_attack' and 'sp_defense'?"
    __msg__.good("Nice work, well done!")
