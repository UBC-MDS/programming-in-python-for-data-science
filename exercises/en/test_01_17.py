def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "loc" in __solution__ , "You don't seem to be using loc."
    assert "Salary" in __solution__, "You did not use Salary in your solution"
    assert 'demko_paid' in __solution__, "You did not name demko_paid properly"
    assert "Age" in __solution__, "You did not use Age in your solution"
    assert 'macewen_age' in __solution__, "You did not name macewen_age properly"
    assert "Position" in __solution__, "You did not use Position in your solution"
    assert 'markstrom_position' in __solution__, "You did not name markstrom_position properly"
    assert "Birth Date" in __solution__, "You did not use Birth Date in your solution"
    assert 'bailey_birth' in __solution__, "You did not name bailey_birth properly"
    
    assert demko_paid == 900000.0, "You did not plot Salary on the correct axis"
    assert macewen_age == 23, "This is the wrong country"
    assert markstrom_position == 'Goalie' , "This is the wrong height"
    assert bailey_birth == '01-Jul-95', "This is the wrong birth date"
    __msg__.good("Nice work, well done!")
