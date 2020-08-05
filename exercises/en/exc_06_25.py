def wage_increase(group):
    new_salary = list()
    raise_increase = list()
    
    for salary in group: 
        new_salary.append(salary * 1.10)
        raise_increase(salary * 0.10)
    
    return new_salary, raise_increase

# Given the function above, improve it so that it follows best function design practices
# Name your new function new_wage()

def new_wage(____):
    return ____

# Test your new function on a person with a salary of $84000 and an expected raise of 12%
# Save this in an object named person1_new_wage

person1_new_wage = ____
person1_new_wage