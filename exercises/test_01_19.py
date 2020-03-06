def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert 'position_column = hockey_players["Position"]' in __solution__ , "There seems to be a problem with finding the column names of the dataset"
    assert "value_counts" in __solution__ , "It looks like you didn't use value_counts"
    assert "sort = True" in __solution__ , "It looks like you didn't specify `sort = True`"
    assert "DataFrame" in __solution__ , "did you convert position_freq to a DataFrame"
    assert "rename" in __solution__ , "did you rename your dataframe?"
    assert '{"Position" : "freq"}' in __solution__ , "There seems to be a problem with the way you renamed your dataframe"
    assert isinstance(temp_df, type(hockey_players)), "temp_df isn't a dataframe"

    assert position_freq_df.shape == (3, 1), "You may not have incorrectly made position_freq_df"
    assert len(position_freq_df) == 3, "Did you use the correct column to make position_freq_df'"
    assert list(position_freq_df.columns) ==  ['freq'], "Your columns do not seem to be correct for position_freq_df"
    assert list(position_freq_df.index) == ['Forward', 'Defense', 'Goalie'], "Your rows do not seem to be correct for position_freq_df"

    assert position_freq_df.iloc[:,0]['Forward'] == 13, "This is the wrong frequency for forward players"
    assert position_freq_df.iloc[:,0]['Defense'] == 7 , "This is the wrong frequency for forward players"
    assert position_freq_df.iloc[:,0]['Goalie'] == 2, "This is the wrong frequency for forward players"
    __msg__.good("Nice work, well done!")

