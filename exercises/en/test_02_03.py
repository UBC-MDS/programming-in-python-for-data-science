def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "index_col=0" in __solution__, "Are you making sure to add index_col=0 ?"
    assert pokemon_df.shape == (801, 11), "The dimensions are incorrect. You may not have the correct dataset"
    assert sorted(list(pokemon_df.columns)) ==  sorted(['deck_no','attack','defense','sp_attack','sp_defense','speed','capture_rt','total_bs','type','gen','legendary']), "Your column names do not seem correct"
    __msg__.good("Nice work, well done!")
