## Prompt: Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
## Return the running sum of nums.

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].



def runningSum( nums):
        
        if len(nums) == 0:
            return 0
        
        sumList = []
        current = 0
        for i in nums:
            current+= i
            sumList.append(current)
            
        return sumList



print(runningSum([1,2,3,4]))
print(runningSum([1,1,1,1,1]))