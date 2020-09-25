def test():
    import inspect
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    
    assert __solution__.count('assert') >= 4, "Make sure you are writing at least four unit tests"
    # Let me know if there are further tests that could be written for this question
    __msg__.good("Nice work, well done!")