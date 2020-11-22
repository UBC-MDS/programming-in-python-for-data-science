def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "hockey_players" in __solution__, "Make sure you are naming your object 'hockey_players'"
    assert "position_bar" in __solution__, "Make sure you are naming your object 'drawer_length'"
    assert hockey_players.shape == (22, 9), "Did you load in 'canucks.csv' correctly?"
    assert position_bar.mark.type == 'bar', "Make sure you are specifying a bar chart using the 'mark_bar()' function"
    assert position_bar.encoding.x.shorthand == 'Position', "Make sure you are specifying the x-axis as `Position` in the '.encode()' function."
    assert position_bar.encoding.y.shorthand == 'count()', "Make sure you are specifying the y-axis as `count()` in the '.encode()' function."
    assert position_bar.mark.opacity == 0.5, "Make sure you are using the 'opacity' parameter and setting it to 0.5"
    assert position_bar.mark.color == 'Teal', "Make sure you are using the 'color' parameter and setting it to 'Teal'"
    assert position_bar.title ==  'Canuck Player Positions', "Make sure you are providing the correct title using the '.properties()' function"    
    __msg__.good("Nice work, well done!")
