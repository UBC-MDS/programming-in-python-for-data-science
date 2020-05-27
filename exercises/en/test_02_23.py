def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "rename" in __solution__ , "Are you using the 'rename' function?"
    assert "assign" in __solution__ , "Are you using the 'assign' function?"
    assert "capture_rate" in __solution__ , "Are you renaming 'capture_rt' to capture_rate?"
    assert "AD_total" in __solution__ , "Are you creating a new column 'AD_total' by adding 'defense' and 'attack'?"
    assert "plot.scatter" in __solution__ , "Are you using 'plot.scatter' as your final chain command?"
    assert list(pokemon_plot.get_ylim()) == [-9.6, 267.59999999999997], "The y-axis limits are incorrect. Is 'capture_rate' on the y-axis?"
    assert list(pokemon_plot.get_xlim()) == [-7.999999999999998, 387.99999999999994], "X-axis limits are incorrect. Is 'AD_total' on the x-axis?"
    __msg__.good("Nice work, well done!")