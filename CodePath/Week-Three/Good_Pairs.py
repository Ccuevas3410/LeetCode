# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.

#  Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.


# O(N^2) solution using double loop

# def numIdenticalPairs (nums):
        
#         if len(nums) == 0:
#             return 0
        
#         count = 0
#         for i in range(len(nums)):
#             for j in range(len(nums)):
                
#                 if nums[i] == nums[j] and i < j:
#                     count+= 1
                    
#         return count
                    
# O(N) solution using dict/hashmap

def numIdenticalPairs (nums):

    hashMap = {}

    count= 0
    for i in nums:

        if i in hashMap:
            count+=hashMap[i]
            hashMap[i]+= 1
            
        else:
            hashMap[i] = 1
             

    return count





print(numIdenticalPairs([1,2,3,1,1,3]))
print(numIdenticalPairs([1,1,1,1]))
print(numIdenticalPairs([1,2,3,]))