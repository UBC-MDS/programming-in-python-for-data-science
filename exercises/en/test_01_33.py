def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed

    assert "age_salary_scatter" in __solution__, "Make sure you are naming your object 'age_salary_scatter'"
    assert age_salary_scatter.mark.type == 'circle', "Make sure you are specifying a scatte plot using the 'mark_circle()' function"
    assert age_salary_scatter.encoding.x.shorthand == 'Age', "Make sure you are specifying the x-axis as `Age` in the '.encode()' function."
    assert age_salary_scatter.encoding.y.shorthand == 'Salary', "Make sure you are specifying the y-axis as `Salary` in the '.encode()' function."
    assert age_salary_scatter.mark.opacity == 0.4, "Make sure you are using the 'opacity' parameter and setting it to 0.4"
    assert age_salary_scatter.mark.color == 'Darkblue', "Make sure you are using the 'color' parameter and setting it to 'Darkblue'"
    assert age_salary_scatter.title ==  'Canuck players Age vs. Salary', "Make sure you are providing the correct title using the '.properties()' function"
    __msg__.good("Nice work, well done!")

