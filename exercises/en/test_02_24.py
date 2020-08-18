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
    assert pokemon_plot.mark == 'circle', "Are you using the 'mark_circle()' function?"
    assert pokemon_plot.encoding.x.shorthand == 'AD_total', "Make sure you are plotting 'AD_total' on the x-axis."
    assert pokemon_plot.encoding.y.shorthand == 'capture_rate', "Make sure you are plotting 'capture_rate' on the y-axis."
    
    __msg__.good("Nice work, well done!")