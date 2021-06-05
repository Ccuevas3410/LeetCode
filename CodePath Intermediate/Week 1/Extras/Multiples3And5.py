# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


# U - > We need to get the multiples of 3 OR 5
# M -> For loop
# P - > The plan is to iterate through the list, and if its a multiple of 3 or 5 we add it to the sum
# I
# R
# E




def multiples():

    i = 0
    total =0
    while i <1000:
        if i%3 == 0 or i%5 ==0:
            total+=i
        i+=1
    return total


print(multiples())
