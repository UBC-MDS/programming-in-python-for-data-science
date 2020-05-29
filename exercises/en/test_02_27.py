def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "groupby" in __solution__ , "Are you using the 'groupby' function?"
    assert "agg" in __solution__ , "Are you chaining the aggregate function with the groupby function?"
    assert "legendary" not in list(legendary_stats.columns), "Are you grouping by 'legendary'?"
    assert "max" in __solution__ , "Are you aggregating by the 'max' value?"
    assert "min" in __solution__ , "Are you aggreating by the 'min' value?"
    assert sum(max(legendary_stats.values.tolist())) == 1563, "Your maximum values are incorrect. Are you aggregating by 'min' and 'max'?"
    assert sum(min(legendary_stats.values.tolist())) == 1679, "Your minimum values are incorrect. Are you aggregating by 'min' and 'max'?"
    __msg__.good("Nice work, well done!")