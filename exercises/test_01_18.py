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

    assert hockey_country == "Canada", "This is the wrong country"
    assert tallest_height == 203 , "This is the wrong height"
    assert youngest_age == 20, "This is the wrong age"
    assert hockey_country == "Canada", "This is the wrong country"
    assert (player_cost == 63325000.0).any, "Did you create player_cost properly?"
    __msg__.good("Nice work, well done!")
