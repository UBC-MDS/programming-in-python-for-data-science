def find_force(mass, acceleration):
    return mass * acceleration

# Take these unit tests compile them together in 
# a function to check the function find_force

assert find_force(50, 3) == 150, 'Input arguments giving incorrect output'
assert find_force(100, -2) == -200, 'Input arguments giving incorrect output'
assert find_force(5, 20) == 100, 'Input arguments giving incorrect output'


____

    return 