def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "character_count" in __solution__, "Make sure you are naming your object 'character_count'."
    assert "character_count = 0" in __solution__, "Make sure you are creating the 'character_count' variable and giving it a value of '0'"
    assert "character_count + len(dish)" in __solution__, "Make sure you are adding 'character_count' to the length of the current dish"
    t = list(__solution__.split()) # transform the solution into a list of string
    for_indices = [i for i, x in enumerate(t) if x == "for"] # get the indices of the for statements
    assert len(for_indices) == 2, "Make sure you are using two for-loops"
    assert for_indices[0] < for_indices[1], "Make sure your for-loops are nested" # Not too sure if this makes a lot of sense.
    assert character_count == 238, "The value for character count is incorrect. Make sure you are adding 'character_count' to the length of the current dish"
    __msg__.good("Nice work, well done!")