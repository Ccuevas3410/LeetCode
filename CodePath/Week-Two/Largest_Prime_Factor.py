#Prompt
#What is the largest prime factor odf the number 600851475143?

#Key Actions
#Find biggest prime factor
#What is the input?
# A number
#What is the data type?
#An integer
#What is the output?
#Largest prime factor

#Where have I seen the problem?
    #Testing for primes
    #Repeating a process for a sequence of numbers (Fibonacci)





#Break down N into all the prime factors, then pick largest
def largest_prime_factor(n):    


    if n < 2:
        return None

    potential_prime_factor = 2
    bigger_prime = 2


#Whilepotential prime factor is not bigger than N
    while potential_prime_factor <=n:

        
#if n mod potential prime factor is equal to 0, this means it is a prime factor
        if  n % potential_prime_factor == 0:
#This is how we will make sure that all the previous prime/composite numbers are taken out of N, so we can move on to the next
            n/=potential_prime_factor
            bigger_prime = potential_prime_factor
           
        else:
            potential_prime_factor += 1

    return bigger_prime

print (largest_prime_factor(26))

     


