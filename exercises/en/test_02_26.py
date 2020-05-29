def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "groupby" in __solution__ , "Are you using the 'groupby' function?"
    assert "mean" in __solution__ , "Are you chaining the mean function with the groupby function?"
    assert "type" not in list(type_means.columns), "Are you grouping by 'type'?"
    assert round(mean_speed.values.mean()) == 68.0, "\nThe average speed values are incorrect. Are you taking the mean after grouping by type?"
    assert round(max(mean_speed.values)) == 100.0, "\nThe maximum average speed is incorrect. Are you taking the mean after grouping by type?"
    __msg__.good("Nice work, well done!")