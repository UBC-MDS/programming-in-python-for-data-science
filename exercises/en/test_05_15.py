def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "character_count" in __solution__, "Make sure you are naming your object 'character_count'."
    assert "character_count = 0" in __solution__, "Make sure you are creating the 'character_count' variable and giving it a value of '0'"
    assert "for category in menu" in __solution__, "Make sure you are interating over 'menu'"
    assert "for dish in category" in __solution__, "Make sure you are interating over 'category'"
    assert "character_count + len(dish)" in __solution__, "Make sure you are adding 'character_count' to the length of the current dish"
    assert character_count == 238, "The value for character count is incorrect. Make sure you are adding 'character_count' to the length of the current dish"
    __msg__.good("Nice work, well done!")