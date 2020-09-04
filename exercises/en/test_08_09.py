def test():
    import inspect
    import numpy as np
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "arr1" in __solution__, "Your object does not exist. Please make sure you are naming your object 'arr1'."
    assert arr1.ndim == 2, "The dimensions of your array are incorrect. Make sure you are creating a 2D array."
    assert arr1.size == 15, "The size of your array is incorrect. Make sure you are creating a 3 by 5 array."
    assert np.count_nonzero(arr1 == 1) == 15.0, "Your array values are incorrect. Make sure you are using the 'np.ones()' function"
    __msg__.good("Nice work, well done!")