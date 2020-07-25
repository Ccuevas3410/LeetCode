# this problem is from project Euler
# https://projecteuler.net/problem=25

# The Fibonacci sequence is defined by the recurrence relation:

#   Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

### PROBLEM STATEMENT ###

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


## Understand:
## 


## Match:


## Plan:

## to get the fib sequence
## start with 0 and 1
## add the last two terms to get the third term
## test how many digits the current term has - if over 1000, return the index of that term
## repeat

## Then, translate to code!



def fibonacci_1000():
    lastNum = 0
    currentNum = 0
    nextNum = 1
    counter = 0
    
    while len(str(currentNum)) != 4:
            lastNum = currentNum
            currentNum = nextNum
            nextNum = lastNum + currentNum
            counter += 1

    print (counter)



fibonacci_1000()



