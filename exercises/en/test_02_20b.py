def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert set(bs_column.values) == {'strong', 'weak'}, "Have you selected the 'base_score' column?"
    assert list(score_freq) == [573, 228], "Count values are incorrect. Are you using the 'count' function?"
    assert "plot.bar" in __solution__ , "Are you using the 'plot.bar' function?"
    assert list(score_plot.get_ylim()) == [0.0, 601.65], "The y-axis limits are incorrect, are you using the 'count' function?"
    assert str(list(score_plot.get_xticklabels())) == "[Text(0, 0, 'weak'), Text(0, 0, 'strong')]", "X-axis labels are incorrect. are you using the 'count' function?"
    __msg__.good("Nice work, well done!")