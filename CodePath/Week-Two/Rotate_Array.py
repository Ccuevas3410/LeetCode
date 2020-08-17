#Prompt
#Given an array. rotate the array to the right by k steps, where k is non-negative
#Key Actions
#Rotate the array to the right by K steps
#What is the input?
# An array of integers and k
#What is the data type?
#An array
#What is the output?
#The rotated array 



def rorate_array(nums,k):

        k = k % len(nums)
        print(k)
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums
        
        
        
        count = 0
        
        


        while count != k:
            
            temp = nums[0]
            nums[0] = nums[-1]
            for i in range( len(nums), 1 , -1):
                nums[i-1] = nums[i - 2]

            nums[1] = temp
            count+= 1
            
        return nums
        

print(rorate_array([1,2,3,4,5],1))