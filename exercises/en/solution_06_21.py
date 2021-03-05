def bmi_calculator(height, weight):
    return (weight/(height**2)) * 702

# Write 4 unit tests and check that at least 2 of them are testing edge cases

assert bmi_calculator(1, 1) == 702.0, 'Input arguments giving incorrect output'
assert bmi_calculator(100, 10000) == 702.0, 'Input arguments giving incorrect output'
assert bmi_calculator(1, 0) == 0, 'Input arguments giving incorrect output'
assert type(bmi_calculator(12,8)) == float, 'Output result type is incorrect'
assert bmi_calculator(20, 400) == 702.0, 'Input arguments giving incorrect output'
assert bmi_calculator(20, 800) == 1404.0, 'Input arguments giving incorrect output'
