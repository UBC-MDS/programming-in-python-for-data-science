# Make a function that takes in the arguments height and weight and returns BMI

def bmi_calculator(height, weight):
    return (weight/(height**2)) * 703


# Use the function to calculate the BMI of a person with height 62 inches and a weight of 105 lbs    
# Save this in an object name bmi_calc

bmi_calc = bmi_calculator(62, 105)

# Display the BMI

bmi_calc 
