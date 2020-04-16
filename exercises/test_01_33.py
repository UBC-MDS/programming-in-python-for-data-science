def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "scatter" in __solution__ , "You don't seem to be plotting a scatterplot"
    assert '"Age"' in __solution__, "You did not use the correct column"
    assert age_salary_scatter.get_ylabel() == 'Salary', "You did not plot Salary on the correct axis"
    assert age_salary_scatter.get_xlabel() == 'Age', "You did not plot Age on the correct axis"
    assert '"Salary"' in __solution__ ,"You did not use the correct column"
    assert '0.4' in __solution__ , "Your alpha value is not correct"
    assert '"Darkblue"' in __solution__ , "Your colour assignment is not correct"
    assert 'title' in __solution__ , "You have not specified a title"
    assert '"Canuck players Age vs. Salary"' in __solution__ , "Your title is not correct"
    __msg__.good("Nice work, well done!")

