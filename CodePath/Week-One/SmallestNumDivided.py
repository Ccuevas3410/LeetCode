#Prompt
#2520 is the smallest numbner than can be divided wby each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive numbner that is evenly divisible b all the numbers from 1 to 20?

#What is the input?
# A range, or really just N from 1 to n.
#What is the data type?
#An integer
#What is the output?
#A number that is divisible by all nums from 1 to 20



def divisibleNum(n):
    ##


  ## So lets find smallest N divisible by 1 2 3


  ## is 4 % 1 = 0? Yes
  ## is 4 % 2 = 0? Yes
  ## is 4 % 3 = 0? No
  ## is 5 % 1 = 0? Yes
  ## is 5 % 2= 0? No
  ## is 6 % 1 = 0? Yes
   ## is 6 % 2 = 0? Yes
    ## is 6 % 3 = 0? Yes

#SO, for every (test number) from 1 to N
# Check if currentNum is divisible by testNum 
#if it is check next test num
# if it is not, increment current num by 1 and start again

    currentNum= n+1
    while True:
        divisible =True
        for test_num in range(2,n+1):
            if currentNum % test_num != 0:
                currentNum+=1
                divisible= False
                break
        if divisible:
                print(currentNum)
                break


divisibleNum(20)