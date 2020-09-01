#
# Complete the 'longestWord' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY words as parameter.
# This function will go through an array of strings, 
# identify the largest word, and return that word. 
#


# Given: ["hello elephants", "hi bugs", "yo snakes"]
# Return: elephants

# Given ["i like potato","acorn","potato acorn"]
# Return: potato





##Though process:
# Go through each subarray of the 2d array and then split the words.
# After they are split, compare the lengths, if any length is bigger than current, save it.
#Do this for each subarray and eventually the largest will be returned
# O(N^2) is the running time. 





def longestWord(words):
    largest = ""
    sentence= ""
    words_separated = ""

    for i in range(len(words)):
        sentence = words.pop(0)
        words_separated = sentence.split(" ")

        for j in words_separated:
            
            if len(j) > len(largest):
                largest = j

    return largest
  
    

print(longestWord(["i like potato", "acorn", "potato acorn"]))