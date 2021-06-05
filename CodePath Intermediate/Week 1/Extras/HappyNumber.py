# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


# U - > We need to get the multiples of 3 OR 5
# M -> While loop
# P - > The plan is to iterate through the list, and if its a multiple of 3 or 5 we add it to the sum
# I -> Done
# R -> 
# E -> Run Time = O(N), Space Complexity = O(1)

