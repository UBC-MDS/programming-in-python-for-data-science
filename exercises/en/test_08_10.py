def test():
    import inspect
    import numpy as np
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "arr2" in __solution__, "Your object does not exist. Please make sure you are naming your object 'arr2'."
    assert "arr2t" in __solution__, "Your object does not exist. Please make sure you are naming your object 'arr2t'."
    assert "sliced_arr2t" in __solution__, "Your object does not exist. Please make sure you are naming your object 'sliced_arr2t'."
    assert arr2.shape == (2, 3), "The dimensions of your array are incorrect. Make sure you are creating a 2D array using the 'reshape()' function."
    assert arr2t.shape == (3, 2), "The dimensions of the transposed array are incorrect. Make sure you are transposing the array properly."
    assert sliced_arr2t.shape == (3,), "The dimensions of the sliced array are incorrect. Make sure you are only slicing the required values."
    assert sum(sliced_arr2t) == 39.0, "The the values in the sliced array are incorrect. Are you slicing properly?"
    __msg__.good("Nice work, well done!")