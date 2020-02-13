def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert ( 
        "model.fit(X,y)"  in __solution__
    ), "Are you sure you used the right functions and parameters?"
    
    assert ( 
        "model.predict(X)"  in __solution__
    ), "Are you sure you used the right functions and parameters?"
    
    __msg__.good("Well done! You successfully trained the data and predicted labels using a machine learning model!")
 