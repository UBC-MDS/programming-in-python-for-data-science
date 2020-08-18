def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "reps" in __solution__, "Make sure you are naming your object 'reps'."
    assert "if exercise == 'lunges':", "Make sure you are including the 'lunges' clause"
    assert "elif exercise == 'squats':", "Make sure you are including the 'squats' clause"
    assert "elif exercise == 'burpees':", "Make sure you are including the 'burpees' clause"
    assert "else:", "Make sure an 'else' statement is part of your conditionals"
    assert reps == 15, "The value of reps is incorrect. Are you setting up your conditionals properly?"
    __msg__.good("Nice work, well done!")