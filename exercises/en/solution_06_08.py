def earth_weight(mass):
    g = 9.8
    weight = mass * g
    return weight

# Create a new function named mass_to_weight() from earth_weight()     
# Give it an additional argument named g which has a default value of 9.8

def mass_to_weight(mass, g=9.8):
    weight = mass * g
    return weight

# Test your new function by converting the mass of 76 kg to weight on Earth     
# Save the results in an object named earth_weight

earth_weight = mass_to_weight(76)
earth_weight

# Test your function again but this time calculate the weight    
# of the 76 kg object on the moon using a gravitational force of 1.62 m/s^2     
# Save your function call to an object named moon_weight

moon_weight = mass_to_weight(76, 1.62) 
moon_weight
