junk_drawer  = [3, 4]

# Using the list provided, add a pen, a scrap paper, a 7.3 and a True element 

junk_drawer.append('pen')
junk_drawer.append('scrap paper')
junk_drawer.append(7.3)
junk_drawer.append(True)

# What's the length of the list now?
# Save it in an object named drawer_length

drawer_length = len(junk_drawer)

# Slice the junk_drawer object to include the element 4 to scrap paper  
# Save this in an object named `cleaned_junk_drawer`

cleaned_junk_drawer = junk_drawer[1:4]

# Next convert it into a set and name it junk_set

junk_set = set(junk_drawer)

junk_set
