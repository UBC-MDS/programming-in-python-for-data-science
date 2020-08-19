def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "def" in __solution__, "Make sure you are defining a function"
    assert "bmi_calculator" in __solution__, "Make sure you are naming your function 'bmi_calculator'"
    assert round(bmi_calc) == 19, "Your function output is incorrect. Are you calculating the 'BMI' correctly?"
    __msg__.good("Nice work, well done!")