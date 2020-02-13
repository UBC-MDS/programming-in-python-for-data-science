def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "obs_total = 16" in __solution__ , "Are you counting the total number of observations in the dataset?"

    assert "obs_peanuts = 6" in __solution__ , "Are you counting the number of observations with peanuts >= 0.5?"

    assert "peanut_america = 5" in __solution__ , "Are you counting the number of observations with peanuts >= 0.5 that are labeled America?"

    assert "peanut_canada = 1" in __solution__ , "Are you counting the number of observations with peanuts >= 0.5 that are labeled America"

    assert "obs_not_peanuts = 10" in __solution__ , "Are you counting the number of observations with peanuts < 0.5?"

    assert "not_peanut_america = 3" in __solution__ , "Are you counting the number of observations with peanuts < 0.5 that are labeled America?"

    assert "not_peanut_canada = 7" in __solution__ , "Are you counting the number of observations with peanuts < 0.5 that are labeled Canada?"

    assert round(peanut_gini_impurity, 2)  == 0.37 , "Are you sure you put your values in the correct place?"
    
    __msg__.good("Well done! You correctly calculated the Gini impurity")
 
