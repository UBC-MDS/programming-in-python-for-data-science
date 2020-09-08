def test():
    import inspect
    import numpy as np
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "lego" in __solution__, "Your object does not exist. Please make sure you are naming your object 'lego'."
    assert "lego_weetabix" in __solution__, "Your object does not exist. Please make sure you are naming your object 'lego_weetabix'."
    assert "lego_cereal" in __solution__, "Your object does not exist. Please make sure you are naming your object 'lego_cereal'."
    assert any("weetabix" in s for s in list(lego_weetabix['name'])), "Make sure you are only selecting 'weetabix' in the 'name' column."
    assert any("cereal-brand" in s for s in list(lego_cereal['name'])), "Make sure you are replacing 'weetabix' with 'cereal-brand'."
    assert not any("promotional" in s for s in list(lego_cereal['name'])), "Make sure you are replacing 'promotional' with 'cereal-brand freebie'."
    __msg__.good("Nice work, well done!")