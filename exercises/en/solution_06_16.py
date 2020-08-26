# Add an exception to the function below that checks if height is of type float and
# an exception that raises an error if weight is 0 or less. 

def bmi_calculator(height, weight):
    if type(height) is not float:
        raise TypeError("Sorry, but you are not using a float for input variable")    
    
    if weight <= 0:
        raise Exception("Weight must be a positive value")

    return (weight/(height**2)) * 702


# Test your function with the values below 

tall = 193
mass = 170.2
