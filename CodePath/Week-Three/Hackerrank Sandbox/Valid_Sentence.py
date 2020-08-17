
#
# Complete the 'isValid' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING sentence as parameter.
# The function will check if the sentence is valid 
# and return true or false accordingly. 
#


#Examples:
# "I like potato" -> Returns False
# "i like potato." -> Returns False
# "I like potato." -> Returns True



def isValid(sentence):
    



    punctuations = ".!?"
    if  not sentence:
        return False

    elif not sentence[0].isupper():
        return False

    elif sentence[-1] not in punctuations:
        return  False
    else:
        return True



print(isValid("I like potato"))
