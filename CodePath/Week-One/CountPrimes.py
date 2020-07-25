

def CountPrimes(n):
    counter = 0
    for i in range (2,n):
        if isPrime(i):
            counter +=1
    return counter

def isPrime(n):
    for current in range(2,n):
        if n % current == 0:
            return False
    return True

print (CountPrimes(10))

#CountPrimes
#Given an input number
# for every number under the input number 
# check to see if number is prime
#if it is, increase counter by one
#else keep going
#return the counter


#isPrime
# is this input prime?
#given an input number
# for every number under n
# check to see if n is evenly divisible by i
# if its not, keep going until true or theres no more number
# if it is divisible, return false;