def test():
    import inspect
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "canucks_altered" in __solution__, "Your object does not exist. Please make sure you are naming your object 'canucks_altered'."
    assert "fillna" in __solution__, "Make sure you are using the 'fillna' function to replace missing values."
    assert "mean()" in __solution__, "Make sure you are replacing missing values with the mean of 'Salary'."
    assert canucks_altered['Salary'].isnull().sum() == 0, "There are still some missing values in the 'Salary' column. Are you filling the missing values?"
    __msg__.good("Nice work, well done!")