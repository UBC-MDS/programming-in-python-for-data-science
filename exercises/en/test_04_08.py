def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "junk_drawer" in __solution__, "Make sure you are naming your object 'junk_drawer'"
    assert "drawer_length" in __solution__, "Make sure you are naming your object 'drawer_length'"
    assert "cleaned_junk_drawer" in __solution__, "Make sure you are naming your object 'cleaned_junk_drawer'"
    assert "junk_set" in __solution__, "Make sure you are naming your object 'junk_set'"
    assert len(
        set(junk_drawer).intersection({3, 4, 7.3, True, 'pen', 'scrap paper'})
    ) == 6, "Some items are missing from 'junk_drawer'. Did you add everything?"
    assert drawer_length == 6, "The length of 'junk_drawer' is incorrect. Did you add everthing?"
    assert len(
        cleaned_junk_drawer
    ) == 3, "The length of 'cleaned_junk_drawer' is incorrect. Are you slicing properly?"
    assert len(
        set(junk_set).intersection({4, 'pen', 'scrap paper'})
    ) == 3, "Some items are missing from 'junk_set'. Are you slicing properly?"
    __msg__.good("Nice work, well done!")
