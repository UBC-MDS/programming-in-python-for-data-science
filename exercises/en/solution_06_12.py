# Make a docstring for the function below: 

def bmi_calculator(height, weight):
    '''
    Calculates and returns the Body Mass Index of an individual 
    
    Parameters
    ----------
    height : float
        The height of an individual in inches
    weight : float
        The weight of an individual in lbs
        
    Returns
    -------
    float
        The Body Mass Index 
        
    Examples
    --------
    >>> bmi_calculator(62, 105)
    19.175338189386057
    '''
    return (weight/(height**2)) * 702

# View the documentation

bmi_calculator?