

#
# Complete the 'FizzBuzz' function below.
#
# This function takes in integer n as a parameter
# and prints out its value, fizz if n is divisible
# by 3, buzz if n divisible by 5, and fizzbuzz 
# if n is divisible by 3 and 5. 
#

#UMPIRE METHOD

#Prompt
#Given an inout, print all numbers up to and including that input, unless they are divisible by 3, then print "Fizz" instead, or if they are divisible by 5, print "buzz." 
# If the number is divisible by both, print "Fizzbuzz"
#Key Actions
#PRINT is the key action, print all numbers including up to the the number,unless number % 3 =  fizz or number % 5 = buzz or fizzbuzz.
#What is the input?
# A number
#What is the data type?
#An integer
#What is the output?
#A number and a string





def FizzBuzz(n):

    for i in range(1,n+1):
        
        if i % 3 == 0:
            if i%5 == 0:
                print("fizzbuzz")
                continue
            print('fizz')
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
                


FizzBuzz(15)
#for every number up to and including the input

   ## if number is divisible by 3, print fizz
   #else if number is divisible by 5, print buzz,
   #is it divisible by 3 and 5?
   #else print the number




