menu = [['Spot Prawn Risotto', 'Atlantic Lobster Bisque',
         'Crab Cake', 'Crisp Calamari'], 
       ['Classic Brown Derby Cobb', 'Spring Garden Salad',
        'Iceberg Wedge'],
       ['Sirloin Steak', 'Pork Chop', 'New York Striploin',
        'Bone-in Rib Steak'],
       ['New York Cheesecake', 'Creme Brulee', 'Key Lime Pie',
        'Carrot Cake', 'Pavlova']]

# Make an object named charater_count and give it a value of 0     

character_count = 0

# Make an outer loop that iterates over each list of the menu list        
# Make an inner loop that iterates over each element in the nested list 
# and add the length of it to charater_count

for category in menu:
    for dish in category:
        character_count = character_count + len(dish)


# Display the value of character_count outside both loops

character_count
