def test():
    import inspect
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "mass_to_weight" in __solution__, "Make sure you are naming your function 'mass_to_weight'"
    arg = inspect.getargspec(mass_to_weight)
    assert len(arg[0]) == 2, "Make sure your function is taking both the weight and the conversion factor" 
    assert arg[0][1] == 'g', "Make sure you are including the parameter 'g' as a function argument"
    assert '9.8' in str(arg), "Make sure you are setting the default value for 'g' to 9.8"
    assert mass_to_weight(100, 7.5) == 750.0, "Your function's output is incorrect. Are you converting correctly?"
    assert round(mass_to_weight(93)) == 911, "Your function's output is incorrect. Are you converting correctly?"
    __msg__.good("Nice work, well done!")