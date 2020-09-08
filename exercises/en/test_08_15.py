def test():
    import inspect
    import numpy as np
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "canucks_info" in __solution__, "Your object does not exist. Please make sure you are naming your object 'canucks_info'."
    assert "canucks_comf" in __solution__, "Your object does not exist. Please make sure you are naming your object 'canucks_comf'."
    assert ".info" in __solution__, "Make sure you are using the '.info()' function to identify null values."
    assert "Wealth" in list(canucks_comf.columns), "Make sure you are creating a new column 'Wealth' in the canucks dataframe."
    assert "comfortable" in set(canucks_comf['Wealth']), "Make sure you are setting the values in the 'Wealth' column to 'comfortable'."
    assert "unknown" in set(canucks_comf['Wealth']), "Make sure you are setting the null values in the 'Wealth' column to 'unknown'."
    assert sum(canucks_comf['Wealth'] == "unknown") == 2, "The amount of 'unknown' values is incorrect. Make ure you are replacing all the null values to 'unknown'."
    __msg__.good("Nice work, well done!")