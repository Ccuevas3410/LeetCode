#Prompt
#Given  an integer, write a function to determine if it is a power of three. Return 1 if the integer is a power of three or 0 if it is not.
#Key Actions
#Return, return 1 if true else 0 if false
#What is the input?
# A number
#What is the data type?
#An integer
#What is the output?
#A number 


# is 3^1=3 a power of three? Yes, return 1
#3^2 = 9 a power of three? Yes, return 1
# 2 a power of three? No, return 0

def isPowerOfThree(n):
    #While n is bigger than 1
    #Keep dividing it
    #if n == 1, then it is a power of three because 3/3 = 1
    #else it is not
  
    while n > 1:
        n = n/3
        if n == 1:
            return True
    return False
        
print(isPowerOfThree(45))