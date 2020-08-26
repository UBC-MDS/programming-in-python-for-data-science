def test():
    import inspect
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "better_kg_to_lb" in __solution__, "Make sure you are naming your function 'better_kg_to_lb'"
    arg = list(inspect.getargspec(better_kg_to_lb))[0]
    assert len(arg) > 0, "Make sure you are passing an argument to your function" 
    assert round(sum(weight_lb_again)) == 913, "Your function output is incorrect. Are you getting rid of side effects?"
    __msg__.good("Nice work, well done!")
