#UMPIRE METHOD

#Prompt
#Given a non-negative number N, return the last digit of the factorial N. This means the product of all the integers from 1 to n
#Key Actions
#Return, return THE LAST DIGIT ofmultiplications of all nums from 1 to N
#What is the input?
# A number
#What is the data type?
#An integer
#What is the output?
#A number 




def last_factorial_digit(n):
    #for every number from 1 to N
    #Multiply 1 x 2 x 3 x N
    #return the multiplication of this
    count = 1
    for i in range(1,n+1):
        count *= i

    return count % 10

print(last_factorial_digit(11))