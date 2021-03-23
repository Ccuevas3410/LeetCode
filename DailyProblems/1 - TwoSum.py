

""" Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass? """


def TwoSumArray(lst, k):
    # Running time: 0(N^2)
    # Space complexity: O(N)
    for i in range(len(lst)):
        target = k - lst[i]
        for j in range(i+1, len(lst)):
            if target == lst[j]:
                return True
    return False


def TwoSum(lst, k):
    # Running time: 0(N)
    # Space complexity: O(N)
    if not lst:
        return False

    dict = {}

    for i in range(len(lst)):
        target = k - lst[i]

        if target in dict:
            return True
        else:
            dict[lst[i]] = 1

    return False


print(TwoSum([], 2))
print(TwoSum([10, 15, 3, 7], 17))
