def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert (player_cost.sum() == 63325000.0).any, "Did you create player_cost properly?"
    __msg__.good("Nice work, well done!")
