def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "ikea_shoe_rack" in __solution__, "Make sure you are naming your result 'ikea_shoe_rack'."
    msg = "Your dictionary contains the incorrect keys. Are you adding all the items? \
    \nExpected ['Long Screw', 'Wood Dowel', 'Short Screw', 'Allen Key'], but got {0}".format(
        list(ikea_shoe_rack.keys()))
    assert sorted(list(ikea_shoe_rack.keys())) == sorted(
        ['Long Screw', 'Wood Dowel', 'Short Screw', 'Allen Key']), msg
    msg = "Your dictionary contains the incorrect values. Are you adding the correct quantities for the items? \
    \nExpected [8, 8, 2, 1], but got {0}".format(
        list(ikea_shoe_rack.values()))
    assert sorted(list(ikea_shoe_rack.values())) == sorted([8, 8, 2, 1]), msg
    __msg__.good("Nice work, well done!")
