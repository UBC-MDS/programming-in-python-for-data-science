def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "tea_amount" in __solution__, "Make sure you are naming your object 'tea_amount'."
    assert "sum(cups_of_tea)", "Make sure you are taking the sum of 'cups_of_tea' before applying the conditionals"
    assert "if type(cups_of_tea)", "Make sure you are checking the type of 'cups_of_tea'"
    assert "else:", "Make sure an 'else' statement is part of your conditionals"
    assert tea_amount == 16, "The value of 'tea_amount' is incorrect. Are you setting up the inline conditional properly?"
    __msg__.good("Nice work, well done!")