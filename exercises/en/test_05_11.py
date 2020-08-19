def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "50" in __solution__, "Make sure your loop is starting at '50'"
    assert "10" in __solution__, "Make sure your loop is  ending at '10'"
    assert "-4" in __solution__, "Make sure you are stepping down by '4' integers at each step"
    assert "2" in __solution__, "Make sure you are squaring each element in the loop" # The are a few ways to square a number in python?
    assert "print" in __solution__, "Make sure you are using the 'print' function to print the values"
    __msg__.good("Nice work, well done!")