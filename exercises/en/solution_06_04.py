weight_kg = [90, 41, 65, 76, 54, 88]
weight_lb = list()

def kg_to_lb(weight_list):
    conversion = 2.20462
    for kg in weight_list:
        weight_lb.append(kg * conversion)
    return 

kg_to_lb(weight_kg)
weight_lb

# rewrite the code and function above so that it does not have any side effects 

def better_kg_to_lb(weight_list):
    weight_lb = list()
    conversion = 2.20462
    
    for kg in weight_list:
        weight_lb.append(kg * conversion)
    return weight_lb

# Test your new function on weight_kg and name the new object weight_lb_again

weight_lb_again = better_kg_to_lb(weight_kg)
weight_lb_again


