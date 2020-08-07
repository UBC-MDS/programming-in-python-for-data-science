def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "pi" in __solution__, "Make sure you are naming your object 'pi'"
    assert "pi_slice" in __solution__, "Make sure you are naming your object 'pi_slice'"
    assert type(
        pi
    ) is float, "Make sure you are converting 'pi' to a float using the 'float()' function."
    assert type(
        pi_slice
    ) is int, "Make sure you are converting 'pi_slice' to a int using the 'int()' function."
    __msg__.good("Nice work, well done!")
