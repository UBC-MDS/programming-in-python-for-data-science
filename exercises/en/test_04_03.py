def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "letitbe_count" in __solution__, "Make sure you are naming your result 'letitbe_count"
    assert "lyrics" in __solution__, "Make sure you are using the 'lyrics' object"
    assert ".lower" in __solution__, "Make sure you are converting to lowercase using the .lower() function."
    assert ".count" in __solution__, "Make sure you are counting the occurences of 'let it be' using the 'count()' function."
    assert letitbe_count == 41, "The occurences of 'let it be' is incorrect. Please try again"
    __msg__.good("Nice work, well done!")
