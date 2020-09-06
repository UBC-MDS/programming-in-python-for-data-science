import numpy as np

# Create an array named arr2 using np.linspace() with 6 equally 
# spaced values from 1 to 16 and a shape of (2,3)

arr2 = np.linspace(1,16,6).reshape(2,3)
arr2

# Transpose the array and name it arr2t

arr2t = arr2.T
arr2t

# Finally slice the new object `arr2t` so it only includes the values 10, 13 and 16
# Save this as an object named sliced_arr2t

sliced_arr2t = arr2t[:,1]
sliced_arr2t

