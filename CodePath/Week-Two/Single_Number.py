# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1






numbers = [1,1,2,2,4,5,5,4,6]

def single_number(nums):
         a = set(nums)
         numMap = {}

         for i in nums:
              if i in numMap:
                 numMap[i] += 1
              else:
                 numMap[i] = 1

         for j in numMap:
             if numMap[j] == 1:
                 return j
              
             

print(single_number(numbers))