def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert hockey_stats.shape == (11, 9), "You may not have selected correctly for hockey_stats"
    assert len(hockey_stats) == 11, "You may not have selected correctly for hockey_stats did you use 'include'"
    assert list(hockey_stats.columns) ==  ['No.', 'Age', 'Height', 'Weight', 'Country', 'Position',
 'Experience', 'Birth Date', 'Salary'], "Your columns do not seem to be correct for hockey_stats"
    assert list(hockey_stats.index) == ['count', 'unique', 'top', 'freq', 
    'mean', 'std', 'min', '25%', '50%', '75%', 'max'], "Your rows do not seem to be correct for hockey_stats"
    __msg__.good("Nice work, well done!")
