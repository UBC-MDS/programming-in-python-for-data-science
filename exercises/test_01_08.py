def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert candybar_feats == ['chocolate', 'peanuts', 'caramel', 'nougat', 'cookie_wafer_rice', 'coconut', 'white_chocolate', 'multi', 'available_canada_america'], "Your features may not be correct, Try putting them in a list and `df.columns` may be useful"
    assert candybar_names == ['CoffeeCrisp', 'Butterfinger', 'Skor', 'Smarties', 'Twix', 'ReesesPeanutButterCups ', '3Musketeers', 'Kinder Surprise', 'M&Ms', 'Glosettes', 'KitKat', 'Babe Ruth', 'Caramilk', 'Aero', 'Mars', 'Payday', 'Snickers', 'Crunchie', 'Wonderbar ', '100Grand ', 'Take5', 'Whatchamacallits', 'AlmondJoy', 'OhHenry', 'CookiesandCream'], "Your candybar names don't seem correct try putting them in a list and `using df.index`"
    assert candybar_dim == (25, 9), "Did you load your data correctly? "
    __msg__.good("Nice work, well done!")
