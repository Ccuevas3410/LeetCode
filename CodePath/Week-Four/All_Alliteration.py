

#
# Complete the 'isAlliteration' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING_ARRAY words as parameter.
# Check if each word in words starts with the same 
# letter and return true or false accordingly. 
#




# Given: ["pack", "peck", "pickled", "peppers"]
# Return: True

# Given ["mary","had","a", "little","lamb"]
# Return: False



##Though process:
# Have a boolean set to True 
# Save the first letter of the first word to be used as the letter EVERY word needs to start with.
# Go through each letter checking ONLY, if the first letter of said word is equal to letter_for_comparison 
# If it is, do nothing until loop ends, if it isnt, return false right away

def isAlliteration(words):
    
    alliteration = True
    letter_for_comparison = words[0][0]

    for i in words:
        if i[0] != letter_for_comparison:
            return False
    return True
    

print(isAlliteration(["pack", "peck", "pickled", "peppers"]))
