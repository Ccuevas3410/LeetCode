#What is the prompt?
    # What is the 10,001st prime number?


# What are the key actions?
    # Printing 10,001st prime num.



# What is the input?
    # A number

# What data type is the input?
    # An integer

# What is the output?
    # An integer

# What is the data type of output ?
    #




#Write a few test cases
    # The first six prime numbers are: 2 3 5 7 9 11 13. We see he 6th prime is 13.

def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True






def nth_prime_number(n):
    counter = 0
    number = 2
    
    while counter != n:
        if isPrime(number):
            counter += 1
            if counter == n:
                return number
            
            number +=1
        else:
            number += 1
           
    return number


print(nth_prime_number(20))



def isPrime_with_list(n, known_primes):
     for i in known_primes:
            if n % i == 0:
                return False
     return True

def nth_prime_codepath(n):
    primes =[]
    number = 2



#While the length of the array is not 

    while len(primes) < n:
        if isPrime_with_list(number, primes):
            primes.append(number)
        number += 1
    return primes[-1]


print(nth_prime_codepath(10001))