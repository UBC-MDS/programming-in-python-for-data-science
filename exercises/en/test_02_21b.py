def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert score_plot.mark == 'bar', "Are you using the 'mark_bar()' function?"
    assert score_plot.encoding.x.shorthand == 'base_score', "Make sure you are plotting 'base_score' on the x-axis."
    assert score_plot.encoding.y.shorthand == 'count()', "Make sure you are using 'count()` to count the occurrences `base_score`."
    __msg__.good("Nice work, well done!")