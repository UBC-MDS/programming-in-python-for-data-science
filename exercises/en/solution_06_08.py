def convert_ounces(original_mass):
    ounces_to_grams = 28.35
    converted_mass = original_mass * ounces_to_grams
    return converted_mass


# Create a new function named convert_mass from convert_ounces() 
# and given it an argument named conversion which has a default value of 28.35.

def convert_mass(original_mass, conversion=28.35):
    converted_mass = original_mass * conversion
    return converted_mass


# Test your function by converting 76 ounces to grams
# Save the results in an object named oz_to_g

oz_to_g = convert_mass(76)

# Test your function using an original mass of 14(kg) and convert it to pounds (lbs)
# using the conversion rate 2.205.       
# Save your function call to an object named kg_to_lbs

kg_to_lbs = convert_mass(14, 2.205) 
kg_to_lbs
