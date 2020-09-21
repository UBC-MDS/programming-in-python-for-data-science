def test():
    import inspect
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "power7_5" in __solution__, "Your object does not exist. Please make sure you are naming your object 'power7_5'."
    assert power7_5 == 16807, "The value for 'power7_5' is incorrect. Are you importing the 'power' function from the 'numpy' library?"
    __msg__.good("Nice work, well done!")