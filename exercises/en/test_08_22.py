def test():
    import inspect
    import numpy as np
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "canucks_upper" in __solution__, "Your object does not exist. Please make sure you are naming your object 'canucks_upper'."
    assert "canucks_upper_ts" in __solution__, "Your object does not exist. Please make sure you are naming your object 'canucks_upper_ts'."
    assert set(canucks_upper['Position']) == {'DEFENSE', 'FORWARD', 'GOALIE'}, "Make sure you are converting the 'Position' column to upper case."
    assert set(canucks_upper['Country']) == {'CANADA', 'FRANCE', 'SWEDAN', 'UNITED STATES'}, "Make sure you are converting the 'Country' column to upper case."
    assert "number_ts" in list(canucks_upper_ts.columns), "The 'number_ts' column does not exist. Please add it to the 'canucks_upper_ts' dataframe."
    assert sum(canucks_upper_ts['number_ts']) == 21, "The values in the 'number_ts' column are incorrect. Are you creating it properly?"
    assert "str.lower()" in __solution__, "You may find the 'str.lower()' function helpful for this question."
    assert "str.upper()" in __solution__, "You may find the 'str.upper()' function helpful for this question."
    __msg__.good("Nice work, well done!")