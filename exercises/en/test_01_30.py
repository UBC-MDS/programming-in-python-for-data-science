def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "value_counts" in __solution__ , "It looks like you didn't use value_counts"
    assert "to_csv" in __solution__ , "It looks like you didn't use to_csv to export your dataframe"
    assert "position_frequencies.csv" in __solution__ , "It looks like you didn't save your dataframe with the correct name"
    assert len(position_freq) ==  3, "Are you using the correct column?"
    __msg__.good("Nice work, well done!")

