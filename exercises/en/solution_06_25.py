def wage_increase(group):
    '''
    Calculates a new wage given a 10% increase for each element in a list and return 
    a list of containing the new salaries and a list of the raise increases
    
    Parameters
    ----------
    group : list
        a list containing a group of people's wages
    
    Returns
    -------
    new_salary : list
        a list containing new salaries after each undergoing a 10% wage increase 
    raise_increase : list 
        a list containing the absolute wage increase each element underwent
    
    Examples
    --------
    >>> wage_increase([20000, 76000, 110000, 88000])
    '''
    new_salary = list()
    raise_increase = list()
    
    for salary in group: 
        new_salary.append(round(salary * 1.10))
        raise_increase.append(round(salary * 0.10))
    
    return new_salary, raise_increase

# Given the function above, improve it so that it follows best function design practices
# Name your new function new_wage()

def new_wage(salary, percent_raise):
    '''
    Calculates a new wage given a percentage
    
    Parameters
    ----------
    salary : int or float
        a salary expected to change
    percent_raise : int or float
        an expect percent which the salary will change
    
    Returns
    -------
    float
        the new salary after undergoing the pay change percentage 
    
    Examples
    --------
    >>> new_wage(30000, 30)
    39000.0
    '''

    return salary * (1 + (0.01 * percent_raise))

# Check your new function on a person with a salary of $84000 and an expected raise of 12%
# Save this in an object named person1_new_wage

person1_new_wage = new_wage(84000, 12)
person1_new_wage