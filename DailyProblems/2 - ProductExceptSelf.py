##Good morning! Here's your coding interview problem for today.
#This problem was asked by Uber.
#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?


def productResultDiv(lst):

# Running time: 0(N)
# Space complexity: O(N)

    if not lst:
        return 0
    productTotal = 1
    result = []
    for i in lst:
        productTotal*=i
    

    for j in lst:
        result.append(productTotal//j)

    return result

#print(productResultDiv([3, 2, 1]))
#print(productResultDiv([1, 2, 3, 4, 5]))


def productResult(lst):
    # Running time: 0(N)
    # Space complexity: O(N)
    if not lst:
            return 0


    productTotal = 1
    result = [1]
    for i in range(1,len(lst)):
        result.append(productTotal)
        productTotal*=lst[i]
    
    right_product = 1

    for j in range(len(lst)-1,-1,-1):
        result[j]*=right_product
        right_product*=lst[j]
    return result

print(productResult([1,2,3,4,5]))