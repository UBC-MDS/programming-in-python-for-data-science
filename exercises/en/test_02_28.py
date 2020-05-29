def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "groupby" in __solution__ , "Are you using the 'groupby' function?"
    assert "type" in __solution__ , "Are you grouping by 'type'?"
    assert "mean" in __solution__ , "Are you chaining the mean function with the groupby function?"
    assert "loc" in __solution__ , "Are you using the loc function to select the 'attack' column?"
    assert "ascending=False" in __solution__ , "Are you sorting in 'decending' order?"
    assert "plot.bar" in __solution__ , "Are you uing the 'plot.bar' function to create a barplot?"
    assert "set_ylabel" in __solution__ , "Are you setting the y-axis label to 'Mean attack score' using the 'set_ylabel' function?"
    __msg__.good("Nice work, well done!")