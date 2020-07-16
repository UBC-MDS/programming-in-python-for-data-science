synonyms = ['cash', 'capital', 'coin', 'dollars', 'money', 'funds', 'stacks']

# Make an empty dictionary named wallet

wallet = dict()

# Make a nest loop that iterates over each word of the list synonyms and 
# iterates over each character in each word

for word in synonyms:
    count = 0
    for letter in word:
        count += 1
    wallet[word] = count


# Display the value of wallet outside both loops.

wallet
