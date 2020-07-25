#Prompt
#Write a program that prints out the Nth value of the Fibonacci sequence

#Key Actions
#Print, print  Nth value if true else 0 if false
#What is the input?
# A number
#What is the data type?
#An integer
#What is the output?
#A number 



def fibonacci(n):
    #For every number  i  from 0 to N+1 ,sum numbers and return number at N index
    #keep adding last value plus new value
    #return n number

    # add last value
    newNum = 0
    currentNum = 0
    nextNum = 1
    for i in range (1, n):

        beforelastNum  = currentNum
        currentNum = nextNum
        nextNum = beforelastNum + currentNum
       

      
    print (currentNum)



    

fibonacci(6)