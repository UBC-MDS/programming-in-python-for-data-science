def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "pokemon_type" in __solution__, "Make sure you are naming your object 'pokemon_type'"
    assert "attack_plot" in __solution__, "Make sure you are naming your object 'attack_plot'"
    assert "groupby" in __solution__ , "Are you using the 'groupby' function?"
    assert "type" in __solution__ , "Are you grouping by 'type'?"
    assert "mean" in __solution__ , "Are you chaining the mean function with the groupby function?"
    assert "loc" in __solution__ , "Are you using the loc function to select the 'attack' column?"
    assert "ascending=False" in __solution__ , "Are you sorting in 'decending' order?"
    assert attack_plot.mark == 'bar', "Make sure you are specifying a scatte plot using the 'mark_bar()' function"
    assert 'type' in attack_plot.encoding.x.shorthand, "Make sure you are specifying the x-axis as `type` in the '.encode()' function."
    assert 'attack' in attack_plot.encoding.y.shorthand, "Make sure you are specifying the x-axis as `attack` in the '.encode()' function."
    __msg__.good("Nice work, well done!")