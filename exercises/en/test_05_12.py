def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "full_dataframe" in __solution__, "Make sure you are naming your object 'full_dataframe'."
    assert "1" in __solution__, "Make sure your loop is starting at '1'"
    assert "5" in __solution__, "Make sure your loop is  ending at '5'"
    assert "str(number)" in __solution__, "Make sure you are converting each number to a string"
    assert "pd.read_csv" in __solution__, "Make sure you are using the 'pd.read_csv()' function to read in the data"
    assert "pd.concat" in __solution__, "Make sure you are using the 'pd.concat()' function concatenate the two dataframes"
    assert full_dataframe.shape[0] == 801 and full_dataframe.shape[1], "The dimensions of 'full_dataframe' are incorrect. Are you reading the concatenating properly?"
    __msg__.good("Nice work, well done!")